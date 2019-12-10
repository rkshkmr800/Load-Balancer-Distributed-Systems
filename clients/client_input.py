#!/lib/python2
import xmlrpclib
import sys, random
import errno
from socket import error as socket_error

try:
	#ip = raw_input("enter ip : ")
	ip = sys.argv[1]
	
	proxy = xmlrpclib.ServerProxy("http://10.5.18."+ip+"/")

	while True:

		x = raw_input("enter x : ")
		y = raw_input("enter y : ")
		p1 = 0.5
		p2 = 0.5
		num_iter = raw_input("enter num_iter : ")
		name = raw_input("enter name : ")
		print ("Finished : ",name ,str(proxy.vary_memory(x,y,p1,p2,num_iter,name, 2)))


	#print "3 is even: %s" % str(proxy.is_even(3))
	#print "100 is even: %s" % str(proxy.is_even(100))

except socket_error as serr:
	if serr.errno == errno.ECONNREFUSED:
		# Not the error we are looking for, re-raise
		print "Server Crashed/Not Available!! Retry Process ", name


