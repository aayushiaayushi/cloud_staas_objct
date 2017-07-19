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
smbuser=data.getvalue('smbuser')
smpass=data.getvalue('smpass')

commands.getstatusoutput('sudo lvcreate -V'+d_size+' --name '+d_name+' --thin smb/smb_pool ')
commands.getstatusoutput('sudo mkfs.ext4 /dev/smb/'+d_name)
commands.getstatusoutput('sudo mkdir /mnt/'+d_name)
commands.getstatusoutput('sudo mount /dev/'+d_name+' /mnt/'+d_name)
commands.getstatusoutput('sudo useradd -s /sbin/nologin '+smbuser)
commands.getstatusoutput('(echo'+smpass+';echo'+smpass+')| sudo smpasswd -a '+smbuser)
entry='['+d_name+']'+'\n'+' path /data/'+d_name+'\n'+'hosts allow = '+cliaddr+'\n'+'valid users ='+smbuser
f=open('/etc/samba/smb.conf','a')
f.write(entry)
f.write('\n')
f.close()

check,check1=commands.getstatusoutput('sudo systemctl restart smb')
if check == 0:
	commands.getstatusoutput('mkdir /media/'+d_name)
	commands.getstatusoutput('mount -o username='+smbuser+ ' //'+s_ip+'/'+d_name+' /media/'+d_name)
	commands.getstatusoutput('sudo touch /var/www/html/samba.sh')
	commands.getstatusoutput('sudo chmod 777 /var/www/html/samba.sh')
	f=open('/var/www/html/samba.sh','w')
	f.write(c)
	f.write('\n')
	f.close()
	commands.getstatusoutput('sudo tar cvf ../html/samba.tar ../html/samba.sh')
	commands.getstatusoutput('sudo chmod 555 ../html/samba.tar')
	print "<META HTTP-EQUIV='refresh' content='0; url=/samba.tar' />"
else:
	print "duplicate entry"
