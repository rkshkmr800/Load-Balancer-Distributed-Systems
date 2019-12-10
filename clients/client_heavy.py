#!/lib/python2
import xmlrpclib
import sys, random
import errno
from socket import error as socket_error


try:
	#ip = raw_input("enter ip : ")
	ip = sys.argv[1]
	
	proxy = xmlrpclib.ServerProxy("http://10.5.18."+ip+"/")

	#while True:

	#x = raw_input("enter x : ")
	x = random.randrange(10000,20000,1000)
	#y = raw_input("enter y : ")
	y = random.randrange(100,800,100)
	#p1 = raw_input("enter p1 : ")
	p1 = 0.1 * random.randrange(6,9,1)
	p2 = 1-p1
	#p2 = raw_input("enter p2 : ")
	#num_iter = raw_input("enter num_iter : ")
	num_iter = random.randrange(10000,15000,1000)
	#name = raw_input("enter name : ")
	name = sys.argv[2]
	print ("msg from server : ",str(proxy.vary_memory(x,y,p1,p2,num_iter,name, 2)))


	#print "3 is even: %s" % str(proxy.is_even(3))
	#print "100 is even: %s" % str(proxy.is_even(100))

except socket_error as serr:
	if serr.errno == errno.ECONNREFUSED:
		# Not the error we are looking for, re-raise
		print "Server Crashed/Not Available!! Retry Process ", name

