#!/usr/bin/python2

import os,cgi,commands,cgitb
cgitb.enable()

print "content-type:text/html"
print  ""
x=cgi.FieldStorage()

saas=x.getvalue('dn')
#print saas
b=(commands.getoutput('hostname -I')).split(' ')
#print b[0]

#print saas
#commands.getoutput('sudo mkdir /var/www/cgi-bin/ankit')
#os.system('sudo touch /var/www/cgi-bin/{}.sh'.format(saas))


if saas == 'firefox' :

#	print saas
	os.chdir("/var/www/html")
	commands.getoutput('sudo touch {}.sh'.format(saas))
	commands.getoutput('sudo chmod 777 {}.sh'.format(saas))
	f=open("/var/www/html/firefox.sh","w")
	f.write("#!/bin/bash")
	f.write("\n ssh -X root@{}   {} \n".format(b[0],saas))
	f.close()


#	print saas
	'''f=open("/var/www/cgi-bin/{}.sh".format(saas),"a")
	f.write("\n ssh -X ankit@{}   {}".format(b[0],saas))
	f.close()
#	print saas
	commands.getoutput("sudo chmod 655 {}.sh".format(saas))
#	print saas'''
	commands.getoutput("sudo tar -cvf {}.tar {}.sh".format(saas,saas)) 
#	commands.getoutput("sudo rm -rf {}.sh".format(saas))			

#	print saas
	
	print "<a href='http://{}/firefox.tar'>".format(b[0])
	os.system('sudo rm -rf /var/www/html/{}.sh'.format(saas))
	print  "<center><b><i>RUN CODE TO GET FIREFOX</b></i></center> "
	print  "</a>"
	print " "
	print "<pre>extract the the downloaded file.\nopen the file in the terminal.\nenter the password.</pre>"

	
elif saas ==  'editor' :

	os.chdir("/var/www/html")
#	print saas
	commands.getoutput('sudo touch {}.sh'.format(saas))
#	print saas
	commands.getoutput('sudo chmod 777 {}.sh'.format(saas))
#	print saas
	f=open("/var/www/html/editor.sh","w")
#	print saas
	f.write("#!/bin/bash")
	f.write("\n ssh -X root@{}   gedit \n".format(b[0]))
	f.close()
	commands.getoutput('sudo tar -cvf {}.tar {}.sh'.format(saas,saas))
#	print saas
	print "<a href='http://{}/editor.tar'>".format(b[0])
	os.system('sudo rm -rf /var/www/html/{}.sh'.format(saas))
	print  "<center><b><i>RUN CODE TO GET EDITOR</b></i></center>"
	print  "</a>"
	print "   "
	print "<pre>extract the the downloaded file.\nopen the file in the terminal.\nenter the password.</pre>"


elif saas == 'calc' :
	
	os.chdir("/var/www/html")
	commands.getoutput('sudo touch {}.sh'.format(saas))
	commands.getoutput('sudo chmod 777 {}.sh'.format(saas))
	f=open("/var/www/html/calc.sh","w")
	f.write("#!/bin/bash")
	f.write("\n ssh -X root@{}   gnome-calculator \n".format(b[0]))
	f.close()
	commands.getoutput('sudo tar -cvf {}.tar {}.sh'.format(saas,saas))
	print "<a href='http://{}/calc.tar'>".format(b[0])
	os.system('sudo rm -rf /var/www/html/{}.sh'.format(saas))
	print "<center><b><i>RUN CODE TO GET CALCULATOR</b></i></center>"
	print "</a>"
	print "   "
	print "<pre>extract the tar downloaded file.\nopen the file in the terminal.\nenter the password.</pre>"


elif saas == 'vlc' :

	os.chdir("/var/www/html")
	commands.getoutput('sudo touch {}.sh'.format(saas))
	commands.getoutput('sudo chmod 777 {}.sh'.format(saas))
	f=open("/var/www/html/vlc.sh","w")
	f.write("#!/bin/bash")
	f.write("\n ssh -X root@{}   vlc \n".format(b[0]))
	f.close()
	commands.getoutput('sudo tar -cvf {}.tar {}.sh'.format(saas,saas))
	print "<a href='http://{}/vlc.tar'>".format(b[0])
	os.system('sudo rm -rf /var/www/html/{}.sh'.format(saas))
	print "<center><b><i>RUN CODE TO GET VLC</b></i></center>"
	print "</a>"
	print "   "
	print "<pre>extract the tar download file.\nopen the file in the terminal.\nenter the password.</pre>"


elif saas == 'office' :

	os.chdir("/var/www/html")
	commands.getoutput('sudo touch {}.sh'.format(saas))
	commands.getoutput('sudo chmod 777 {}.sh'.format(saas))
	f=open("/var/www/html/office.sh","w")
	f.write("#!/bin/bash")
	f.write("\n ssh -X root@{}   libreoffice \n".format(b[0]))
	f.close()
	commands.getoutput('sudo tar -cvf {}.tar {}.sh'.format(saas,saas))
	print "<a href='http://{}/office.tar'>".format(b[0])
	os.system('sudo rm -rf /var/www/html/{}.sh'.format(saas))
	print "<center><b><i>RUN CODE TO GET OFFICE</b></i></center>"
	print "</a>"
	print "   "
	print "<pre>extract the tar download file.\nopen the file in the terminal.\nenter the password.</pre>"


else :
	print "<center><b>Consult SINHA</b></center>"


