#!/usr/bin/python2

import  cgi,commands

print "content-type:text/html"
print  ""
b=(commands.getoutput('hostname -I')).split(' ')

x=cgi.FieldStorage()

c_service=x.getvalue('dn')

if c_service == 'saas' :
	print "<a href='http://{}/saas.html'>".format(b[0])
	print "<center>"
	print  "<b><i>ACCESS SAAS CLOUD</b></i>"	
	print "</center>"
	print  "</a>"

elif c_service ==  'staas' :
	print "<a href='http://{}/staas.html'>".format(b[0])
	print "<center>"
	print  "<b><i>ACCESS StAAS CLOUD</b></i>"
	print "</center>"
	print  "</a>"

elif c_service == 'pass' :
	print "<a href='http://{}/paas.html'>".format(b[0])
	print "<center>"
	print "<b><i>ACCESS PAAS CLOUD</b></i>"
	print "</center>"
	print "</a>"

elif c_service == 'iaas' :
	print "<a href='http://{}/iaas.html'>".format(b[0])
	print "<center>"
	print "<b><i>ACCESS IAAS CLOUD</b></i>"
	print "</center>"
	print "</a>"

