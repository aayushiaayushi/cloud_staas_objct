#! /usr/bin/python

import cgi,cgitb,os,time,commands,sys
cgitb.enable()
print "Content-type:text/html"
print ""

x=cgi.FieldStorage()
#here setup choice will store

choice=x.getvalue('choose')

if choice == 'linux':
	print "<META HTTP-EQUIV='refresh' content='0; url=/staas_object.html' />"
elif choice == 'win':
	print "<meta http-equiv='refresh' content='0;url=/block.html'>"

