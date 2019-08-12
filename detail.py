#!/usr/bin/python2

import  cgi,os,cgitb,commands
cgitb.enable()

z=(commands.getoutput('hostname -I')).split(' ')

print "content-type:text/html"
print  ""

x=cgi.FieldStorage()

user=x.getvalue('dn')
password=x.getvalue('ds')

if user == 'root' and  password == 'redhat' :

	print "<a href='http://{}/service.html'>".format(z[0])
	print "<center>"
	print  "<b><i>GO TO CLOUD SERVICE PAGE</b></i>"
	print "</center>"	
	print  "</a>"

else :
	print  "bad details plz try again "
	print  "<a href='http://{}'>".format(z[0])
	print  "Click here to try again"
	print  "</a>"

