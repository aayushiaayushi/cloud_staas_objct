#! /usr/bin/python

import cgi,cgitb,os,time,commands,sys
cgitb.enable()
print "Content-type:text/html"
print ""

x=cgi.FieldStorage()
#here setup choice will store

choice=x.getvalue('choose')

if choice == 'object':
	print "<html><meta http-equiv='refresh' content='0;url=/staas_ser.html'></html>"
elif choice == 'block':
	print "<meta http-equiv='refresh' content='0;url=/staas_block.html'>"

