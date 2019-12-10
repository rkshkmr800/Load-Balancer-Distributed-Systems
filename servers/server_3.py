# from __future__ import print_function
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from time import sleep
import psutil
import threading
import numpy as np
from math import sqrt, log
import sys

import errno
from socket import error as socket_error
import codecs

nbr_IPs = ["http://10.5.18.102:10000/", "http://10.5.18.102:8000/", "http://10.5.18.103:8000/"]

own_IP = "http://10.5.18.102:9000/"

CV_TH = 0.25

DICT_SERVER_NO = {"http://10.5.18.102:10000/": '1', "http://10.5.18.102:8000/": '2', "http://10.5.18.102:9000/": '3', "http://10.5.18.103:8000/": '4', "http://10.5.18.103:9000/": '5', "http://10.5.18.103:10000/": '6'}


p = psutil.Process()

import SocketServer

CRED = '\033[91m'
CGREEN = '\33[92m'
CGREENBG2  = '\33[102m'
CREDBG2 = '\33[101m'
CBLUE = '\33[94m'
CBOLD = '\33[1m'
CEND = '\033[0m'
CBLUEBG2   = '\33[104m'


log_file = codecs.open('log_dir/server_'+DICT_SERVER_NO[own_IP]+'.txt', 'a', 'utf-8')

class AsyncXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer): pass

class RequestHandler(SimpleXMLRPCRequestHandler):
	def log_message(self, format, *args):
		return

def removekey(d, key):
	r = dict(d)

	# if key in r.items():
	r.pop(key, None)
	# del r[key]
	return r

def print_nbr_load():
	global loads_at_nbrs

	s = '[ '

	for nbr in loads_at_nbrs:
		if nbr != own_IP:
			s = s + DICT_SERVER_NO[nbr] + ':'+str(round(loads_at_nbrs[nbr][1], 2))+', '

	s = s+']'

	return s

def send_current_load():
	global p, curr_nbr_loads, loads_at_nbrs

	curr_vec = []

	for nbr in loads_at_nbrs:
		curr_vec.append(loads_at_nbrs[nbr][1])

	if len(curr_vec) != 0:
		mean = sum(curr_vec) / (1.0*len(curr_vec))
	else:
		mean = 0
	curr_mem = p.memory_info()[0]/1000000.0

	final_mean = (curr_mem + mean)/2.0
	return (round(curr_mem, 2), round(final_mean, 2))


def collect_nbr_load():
	global loads_at_nbrs, p, curr_nbr_loads, curr_nbr_means, log_file, nbr_server_proxies

	sleep(10)

	nbr_server_proxies = {}

	loads_at_nbrs = {}

	for nbr in nbr_IPs:
		try:
			nbr_server_proxies[nbr] = xmlrpclib.ServerProxy(nbr)
		except Exception as e:
			print 'Error connecting to: ', nbr, str(e)


	idx = -1

	FLAG_NBR = {}

	for nbr in nbr_IPs:
		FLAG_NBR[nbr] = 0

	while True:

		# print('Collecting Load From Servers....')

		for nbr in nbr_IPs:
			try:
				nbr_server_proxies[nbr] = xmlrpclib.ServerProxy(nbr)
				loads_at_nbrs[nbr] = nbr_server_proxies[nbr].send_current_load()

				if FLAG_NBR[nbr] == 1:
					FLAG_NBR[nbr] = 0

			except Exception as e:
				# if serr.errno == errno.ECONNREFUSED:
				if FLAG_NBR[nbr] == 0:
					print 'Error getting info from: ', nbr, str(e)
					FLAG_NBR[nbr] = 1
					loads_at_nbrs = removekey(loads_at_nbrs, nbr)
					nbr_server_proxies = removekey(nbr_server_proxies, nbr)


		curr_nbr_loads = []
		curr_nbr_means = []

		curr_nbr_loads.append(p.memory_info()[0]/1000000.0)


		for nbr in loads_at_nbrs:
			curr_nbr_loads.append(loads_at_nbrs[nbr][0])
			curr_nbr_means.append(loads_at_nbrs[nbr][1])

		# curr_nbr_loads.sort()

		curr_mem = p.memory_info()[0]/1000000.0

		final_vec = curr_nbr_means + [curr_mem]

		# calculate mean
		m = sum(final_vec) / len(final_vec)

		if m == 0:
			m = 1.0

		# calculate variance using a list comprehension
		var_loads = sum([(xi - m) ** 2 for xi in final_vec]) / len(final_vec)

		std_dev = sqrt(var_loads)

		coeff_var = std_dev / abs(m)

		print_str = 'My Load: '+ str(round(curr_mem, 2))+', NBRS:'+print_nbr_load()+', C_V: '+str(round(coeff_var, 3))+'\n'

		if idx < 5 or idx%5 == 0:
			print >>sys.stderr, print_str, 
		
		log_file.write('LOAD_COLLECTION\t'+print_str)
		
		sleep_time = 5.0/(log(p.memory_info()[0]/1000000.0, 2))

		# print  'Next Load collection after:', sleep_time, 'My Load:', p.memory_info()[0]/1000000.0
		sleep(sleep_time)
		idx += 1


def select_transfer_node(incoming_IP):
	global loads_at_nbrs, p, curr_nbr_loads, curr_nbr_means, nbr_server_proxies

	curr_mem = p.memory_info()[0]/1000000.0

	final_vec = curr_nbr_means + [curr_mem]

	m = sum(final_vec) / len(final_vec)

	if m == 0:
		m = 1.0

	# calculate variance using a list comprehension
	var_loads = sum([(xi - m) ** 2 for xi in final_vec]) / len(final_vec)

	std_dev = sqrt(var_loads)

	coeff_var = std_dev / abs(m)


	if coeff_var > CV_TH:

		curr_vec = {}

		for nbr in loads_at_nbrs:
			curr_vec[nbr] = loads_at_nbrs[nbr][1]

		curr_vec[own_IP] =  curr_mem

		# curr_vec.sort()


		# loads_at_nbrs[own_IP] = (curr_mem, curr_mem)

		sorted_loads = sorted(curr_vec.items(), key = lambda x: x[1])

		for elem in sorted_loads:
			if elem[0] == incoming_IP:
				continue
			t_node = elem[0]

			if t_node == own_IP:
				print_str = CBLUE+'Curr C_V: '+ str(round(coeff_var, 3))+', My Load: '+str(round(curr_mem, 2))+', '+print_nbr_load()+CEND+'\n'
				print >>sys.stderr, print_str,
			else:
				print_str = CRED+'C_V: '+ str(round(coeff_var, 3)) + ', My Load: ' + str(round(curr_mem, 2)) + ', Trg Load:' + str(elem[1]) +  ', Nbrs:' + print_nbr_load() + CEND + '\n'
				print >>sys.stderr, print_str,
			return elem[0]

	else:
		return own_IP


def vary_memory(x, y, p1, p2, num_iter, client_name, TTL):
	global loads_at_nbrs, nbr_server_proxies, log_file

	# for nbr in nbr_IPs:
	# 	try:
	# 		curr_connec = xmlrpclib.ServerProxy(nbr)
	# 		loads_at_nbrs[nbr] = curr_connec.send_current_load()

	# 	except Exception as e:
	# 		print 'Error getting info from: ', nbr, str(e)

	if len(client_name.strip().split("_")) == 1:
		print_str = CBLUE+'New Request from Client: '+CEND + CBOLD + client_name + CEND + '\n'
		print_file_str = 'New Request from Client: ' + client_name + '\n'
		print >>sys.stderr, print_str,

		log_file.write('NEW_CLIENT_REQ_1'+'\t'+print_file_str)

		client_print_name = client_name

	else:
		client_print_name = client_name.split("_")[0] + "_" + DICT_SERVER_NO[client_name.split("_")[-1]]
		print_str = CBLUEBG2+'Forwarded Request from Server: ' + CEND + CBOLD + DICT_SERVER_NO[client_name.split("_")[-1]] + ', ' + client_print_name + CEND + '\n'
		print_file_str = 'Forwarded Request from Server: ' + DICT_SERVER_NO[client_name.split("_")[-1]] + '\n'
		print >>sys.stderr, print_str,

		log_file.write('NEW_FORWARDED_REQ'+'\t'+print_file_str)

		

	if TTL > 0:
		while True:
			try:
				t_node = select_transfer_node(client_name.split("_")[-1])


				if t_node == own_IP:
					break

				else:
					print_str = CRED+"Transferring "+ CEND + CBOLD + client_print_name + CEND + CRED + " to: "+ CEND + CBOLD + DICT_SERVER_NO[t_node] + CEND + CRED + ", Function: vary_memory, Parameters:" + str(x) + ',' + str(y) + ',' + str(num_iter) +',' + client_print_name +',' + str(TTL-1) + CEND + '\n'
					print_file_str = "Transferring " + client_print_name + " to: "+ DICT_SERVER_NO[t_node] + ", Function: vary_memory, Parameters:" + str(x) + ',' + str(y) +',' + str(num_iter) +',' + client_print_name +',' + str(TTL-1) + '\n'
					print >>sys.stderr, print_str,

					log_file.write('TRANSFER_REQ'+'\t'+print_file_str)

					t_node_server = xmlrpclib.ServerProxy(t_node)
					output = t_node_server.vary_memory(x, y, p1, p2, num_iter, client_print_name+"_"+own_IP, TTL-1)
					print_str = "Retrieved from: " + DICT_SERVER_NO[t_node] + ", Output: " + str(output) + '\n'
					print >>sys.stderr, print_str,

					print_str =  CGREEN+'Returning to Client: ' + CEND + CBOLD + client_print_name + CEND + CGREEN + ', output:'+ str(output) + CEND + '\n'

					print_file_str = "Returning to Client: " + client_print_name + ", Output: " + str(output) + '\n'

					log_file.write('RETURN_TO_CLIENT'+'\t'+print_file_str)

					print >>sys.stderr, print_str,

					return output

			except xmlrpclib.ProtocolError as exc:
				# print("ERROR!!!!!!!:",str(e))
				# if serr.errno == errno.ECONNREFUSED:
				print_str = CREDBG2+'Server '+DICT_SERVER_NO[t_node] + ' crashed!! Selecting different node for executing '+CEND + CBOLD + client_print_name + CEND+'\n'
				print >>sys.stderr, print_str,

				print_file_str = 'Server '+DICT_SERVER_NO[t_node] + ' crashed!! Selecting different node for executing '+ client_print_name + '\n'

				log_file.write('SERVER_CRASH'+'\t'+print_file_str)

				loads_at_nbrs = removekey(loads_at_nbrs, t_node)
				nbr_server_proxies = removekey(nbr_server_proxies, t_node)




	print_str = CGREEN+'Executing ' + CEND + CBOLD + client_print_name + CEND + CGREEN +' '+ str(x) + ',' + str(y) +',' + str(num_iter) +',' + client_print_name +',' + str(TTL-1) + CEND + '\n'
	print_file_str = 'Executing ' + client_print_name + ' '+ str(x) + ',' + str(y) +',' + str(num_iter) +',' + client_print_name +',' + str(TTL-1) + '\n'
	print >>sys.stderr, print_str,

	log_file.write('REQ_EXEC_1'+'\t'+print_file_str)

	x = int(x)
	y = int(x)
	p1 = float(p1)
	p2 = float(p2)
	num_iter = int(num_iter)
	# p3 = float(p3)


	probs = [p1, p2]

	probs = np.asarray(probs)

	probs = probs/(1.0*probs.sum())
	
	li = []


	for idx in range(num_iter):
		# sampled_val == random.
		sampled_val = np.random.choice(range(2), 1)
		if sampled_val == 0:
			li += [1.1] * x
			# print "in"
		else:
			li = li[:len(li) - y]
		
		# idx += 1

		# if idx%1000 == 0:
		# 	print 'Client:', client_name, 'idx:', idx, 'li_len:', len(li)

	print_str = CGREEN+'Returning to Client: ' + CEND + CBOLD + client_print_name + CEND + CGREEN + ', output:'+ str(len(li)) + CEND + '\n'
	print_file_str = "Returning to Client: " + client_print_name + ", Output: " + str(len(li)) + '\n'

	print >>sys.stderr, print_str,

	log_file.write('RETURN_TO_CLIENT'+'\t'+print_file_str)

	li_len = len(li)

	del li

	return li_len



def uniform_memory(x, num_iter, client_name, TTL):
	global loads_at_nbrs, log_file, nbr_server_proxies

	if len(client_name.strip().split("_")) == 1:
		print_str = CBLUE+'New Request from Client: '+CEND + CBOLD + client_name + CEND + '\n'
		print_file_str = 'New Request from Client: '+ client_name + '\n'
		print >>sys.stderr, print_str,

		log_file.write('NEW_CLIENT_REQ_2'+'\t'+print_file_str)

		client_print_name = client_name

	else:
		client_print_name = client_name.split("_")[0] + "_" + DICT_SERVER_NO[client_name.split("_")[-1]]
		print_str = CBLUEBG2+'Forwarded Request from Server: ' + CEND + CBOLD + DICT_SERVER_NO[client_name.split("_")[-1]] + ', ' + client_print_name + CEND + '\n'
		print_file_str = 'Forwarded Request from Server: ' + DICT_SERVER_NO[client_name.split("_")[-1]] + '\n'
		print >>sys.stderr, print_str,

		log_file.write('NEW_FORWARDED_REQ'+'\t'+print_file_str)
		
		# client_print_name = client_name.split("_")[0] + "_" + DICT_SERVER_NO[client_name.split("_")[-1]]

	if TTL > 0:
		while True:
			try:
				t_node = select_transfer_node(client_name.split("_")[-1])


				if t_node == own_IP:
					break

				else:
					print_str = CRED+"Transferring "+ CEND + CBOLD + client_print_name + CEND + CRED + " to: "+ CEND + CBOLD + DICT_SERVER_NO[t_node] + CEND + CRED + ", Function: uniform_memory, Parameters:" + str(x) + ',' + str(num_iter) +',' + client_name +',' + str(TTL-1) + CEND + '\n'
					print_file_str = "Transferring "+ client_print_name + " to: "+ DICT_SERVER_NO[t_node] + ", Function: uniform_memory, Parameters:" + str(x) + ',' + str(num_iter) +',' + client_name +',' + str(TTL-1) + '\n'
					print >>sys.stderr, print_str,

					log_file.write('TRANSFER_REQ'+'\t'+print_file_str)

					t_node_server = xmlrpclib.ServerProxy(t_node)
					output = t_node_server.uniform_memory(x, num_iter, client_print_name+"_"+own_IP, TTL-1)
					print_str = "Retrieved from: " + DICT_SERVER_NO[t_node] + ", Output: " + str(output) + '\n'
					print >>sys.stderr, print_str,

					print_str =  CGREEN+'Returning to Client: ' + CEND + CBOLD + client_print_name + CEND + CGREEN + ', output:'+ str(output) + CEND + '\n'
					print >>sys.stderr, print_str,

					print_file_str = "Returning to Client: " + client_print_name + ", Output: " + str(output) + '\n'

					log_file.write('RETURN_TO_CLIENT'+'\t'+print_file_str)

					return output

			except xmlrpclib.ProtocolError as exc:
				# print("ERROR!!!!!!!:",str(e))
				# if serr.errno == errno.ECONNREFUSED:
				print_str = CREDBG2+'Server '+DICT_SERVER_NO[t_node] + ' crashed!! Selecting different node for executing '+CEND + CBOLD + client_print_name + CEND+'\n'
				print >>sys.stderr, print_str,

				print_file_str = 'Server '+DICT_SERVER_NO[t_node] + ' crashed!! Selecting different node for executing '+ client_print_name + '\n'

				log_file.write('SERVER_CRASH'+'\t'+print_file_str)

				loads_at_nbrs = removekey(loads_at_nbrs, t_node)
				nbr_server_proxies = removekey(nbr_server_proxies, t_node)


	print_str = CGREEN+'Executing ' + CEND + CBOLD + client_print_name + CEND + CGREEN +' '+ str(x) +',' + str(num_iter) +',' + client_name +',' + str(TTL-1) + CEND + '\n'
	print >>sys.stderr, print_str,

	print_file_str = 'Executing ' + client_print_name +' '+ str(x) +',' + str(num_iter) +',' + client_name +',' + str(TTL-1) + '\n'
	log_file.write('REQ_EXEC_2'+'\t'+print_file_str)

	x = int(x)
	num_iter = int(num_iter)
	# p3 = float(p3)

	
	li = []


	for idx in range(num_iter):
		li += [1.1] * x


	sleep(80)

	print_str = CGREEN+'Returning to Client: ' + CEND + CBOLD + client_print_name + CEND + CGREEN + ', output:'+ str(len(li)) + CEND + '\n'
	print_file_str = "Returning to Client: " + client_print_name + ", Output: " + str(len(li)) + '\n'

	print >>sys.stderr, print_str,

	log_file.write('RETURN_TO_CLIENT'+'\t'+print_file_str)

	li_len = len(li)

	del li

	return li_len

def vary_memory_thread(x, y, p1, p2, p3, client_name):

	t_1 = threading.Thread(target=vary_memory, args = (x, y, p1, p2, p3, client_name))

	t_1.start()

	t_1.join()	


def add_10(n, TTL):
	incoming_IP = ""

	if TTL > 0:
		t_node = select_transfer_node(incoming_IP)

		if t_node == -1:
			pass

		else:
			print "Transferring Task to:", t_node, "Function: add_10, Parameters:", n, TTL
			t_node_server = xmlrpclib.ServerProxy(t_node)
			output = t_node_server.add_10(n, TTL-1)
			print "Retrieved from ", t_node, "Output: ", output
			print "Returning to Client"
			return output

	curr_no = int(n)

	# sleep(curr_no)

	print "msg from client :",curr_no
	curr_no += 10
	return curr_no


curr_nbr_loads = []
curr_nbr_means = []
loads_at_nbrs = {}
# parse_docs()

server = AsyncXMLRPCServer((own_IP.split("/")[2].split(":")[0], int(own_IP.split("/")[2].split(":")[1])), RequestHandler)
print "Listening on IP:", own_IP.split("/")[2].split(":")[0], "Port:", int(own_IP.split("/")[2].split(":")[1])
server.register_function(add_10, "add_10")
server.register_function(vary_memory, "vary_memory")
server.register_function(uniform_memory, "uniform_memory")
server.register_function(send_current_load, "send_current_load")
print "Registered Functions"

start_now = raw_input("Start Server[y/n]:")

print('Server Started....Press Ctrl+C to exit....')

t_collect = threading.Thread(target=collect_nbr_load)

t_collect.start()


print "Serving"

server.serve_forever()

# t_collect.join()
