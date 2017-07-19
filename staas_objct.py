#! /usr/bin/python

import cgi,cgitb,os,time,commands,sys
cgitb.enable()
print "Content-type:text/html"
print ""
s_ip='192.168.122.100'
data=cgi.FieldStorage()
#here setup choice will store

d_name=data.getvalue('dname')
d_size=data.getvalue('dsize')
cliaddr=data.getvalue('cliaddr')

commands.getstatusoutput('sudo lvcreate -V'+d_size+' --name '+d_name+' --thin adhocvg/pool1 ')
commands.getstatusoutput('sudo mkfs.ext4 /dev/adhocvg/'+d_name)
commands.getstatusoutput('sudo mkdir /mnt/'+d_name)
commands.getstatusoutput('sudo mount /dev/adhocvg/'+d_name+' /mnt/'+d_name)
entry="/mnt/"+d_name+" "+cliaddr+"(rw,no_root_squash)"
f=open('/etc/exports','a')
f.write(entry)
f.write('\n')
f.close()

commands.getstatusoutput('sudo systemctl restart nfs-server')
commands.getstatusoutput('sudo systemctl enable nfs-server')

check,check1=commands.getstatusoutput('sudo exportfs -r')
if check == 0: 
	c='mkdir /media/'+d_name+'\n'+'mount '+cliaddr+':/mnt/'+d_name+' /media/'+d_name
	commands.getstatusoutput('sudo touch /var/www/html/obbulk.sh')
	commands.getstatusoutput('sudo chmod 777 /var/www/html/obbulk.sh')
	f=open('/var/www/html/obbulk.sh','w')
	f.write(c)
	f.write('\n')
	f.close()
	commands.getstatusoutput('sudo tar -cvf ../html/obbulk.tar ../html/obbulk.sh')
	commands.getstatusoutput('sudo chmod 555 ../html/obbulk.tar')
	print "<META HTTP-EQUIV='refresh' content='0; url=/obbulk.tar' />"
else:
	print "duplicate entry"
