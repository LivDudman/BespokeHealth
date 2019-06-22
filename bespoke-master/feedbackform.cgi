#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html\n"


form = cgi.FieldStorage()

name = form.getvalue("fullname")
course = form.getvalue("course")
date = form.getvalue("date")
email = form.getvalue("email")
feedback = form.getvalue("feedback")

print """
<!doctype html>
<html>
<head>
	<title>Thank You!</title>
</head>

<body>
<p><strong>Thank you {0} for your feedback"</strong></p>

</body>
</html> 

""".format(name)
