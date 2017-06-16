#! /usr/bin/python

import socket,sys,os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
drive_nme=raw_input("enter drive name:")
drive_size=raw_input("enter size of drive:")
s_ip="192.168.122.3"
s_port=8888
s.sendto(drive_nme,(s_ip,s_port))
s.sendto(drive_size,(s_ip,s_port))
resp=s.recvfrom(20)
if resp[0] == "done":
	os.system('mkdir  /media/'+drive_nme)
	os.system('mount   '+s_ip+':/mnt/'+drive_nme+'   /media/'+drive_nme)
else:
	print "No response "
