#! /usr/bin/python

import socket,sys,os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("",8888))
#receiving drive name from data
data=s.recvfrom(20)
d_name=data[0]

#receiving drive size from data1
data1=s.recvfrom(20)
d_size=data1[0]
#client's address
cliaddr=data[1][0]
#creating LVM by name of client drive 
os.system('lvcreate --name '+d_name+' --size '+d_size+'M  noavg')

#now format the drive
os.system('mkfs.xfs /dev/noavg/'+d_name)
#now creating mounting point
os.system('mkdir /mnt/'+d_name)
#mounting locally
os.system('mount /dev/noavg/'+d_name+'  /mnt/'+d_name)
#now configuration of NFS server
#os.system('yum install nfs-utils -y')
#making entry in NFS file
entry="/mnt/"+d_name+" "+cliaddr+"(rw,no_root_squash)"
#appending this var to /etc/exports file
f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()

#starting nfs service
check=os.system('exportfs -r')
if check == 0:
	s.sendto("done",data1[1])
else:
	print "check your code"
