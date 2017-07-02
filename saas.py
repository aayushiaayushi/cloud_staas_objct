#! /usr/bin/python

import cgi,cgitb,os,time,commands,sys

print "content-type:text/html"
print "";

x=cgi.FieldStorage()
#here setup choice will store

choice=x.getvalue('choose')

if choice == 'firefox':
	os.system('echo sshpass -p 123 ssh -X test@192.168.10.102 firefox'+'>>'+' firefox.sh')
	os.system('chmod +x firefox.sh')
	os.system(' tar cvf'+' /html/firefox.tar'+' firefox.sh')
	print "<html><meta http-equiv='refresh' content='0;url=/firefox.tar'></html>"	

elif choice == 'vlc':
	os.system('echo sshpass -p 123 ssh -X test@192.168.10.102 vlc'+'>>'+' vlc.sh')
	os.system('chmod +x vlc.sh')
	os.system(' tar cvf'+' /html/vlc.tar'+' vlc.sh')
	print "<html><meta http-equiv='refresh' content='0;url=/vlc.tar'></html>"	


elif choice == 'calculator':
	os.system('echo sshpass -p 123 ssh -X test@192.168.10.102 gnome-calculator'+'>>'+' calculator.sh')
	os.system('chmod +x calculator.sh')
	os.system(' tar cvf'+' /html/calculator.tar'+' calculator.sh')
	print "<html><meta http-equiv='refresh' content='0;url=/calculator.tar'></html>"	


elif choice == 'webcam':
	os.system('echo sshpass -p 123 ssh -X test@192.168.10.102 cheese'+'>>'+' webcam.sh')
	os.system('chmod +x webcam.sh')
	os.system(' tar cvf'+' /html/webcam.tar'+' webcam.sh')
	print "<html><meta http-equiv='refresh' content='0;url=/webcam.tar'></html>"	


elif choice == 'Imageviewer':
	os.system('echo sshpass -p 123 ssh -X test@192.168.10.102 Imageviewer'+'>>'+' Imageviewer.sh')
	os.system('chmod +x Imageviewer.sh')
	os.system(' tar cvf'+' /html/Imageviewer.tar'+' Imageviewer.sh')
	print "<html><meta http-equiv='refresh' content='0;url=/Imageviewer.tar'></html>"	


elif choice == 'Libreoffice':
	os.system('echo sshpass -p 123 ssh -X test@192.168.10.102 openoffice'+'>>'+' Libreoffice.sh')
	os.system('chmod +x Libreoffice.sh')
	os.system(' tar cvf'+' /html/Libreoffice.tar'+' Libreoffice.sh')
	print "<html><meta http-equiv='refresh' content='0;url=/Libreoffice.tar'></html>"	






