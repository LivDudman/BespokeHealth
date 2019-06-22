#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html\n"


form = cgi.FieldStorage()

fullname = form.getvalue("fname")
tel = form.getvalue("tel")
time = form.getvalue("morning")
time = form.getvalue("midday")
time = form.getvalue("evening")
time = form.getvalue("anytime")
enquiry = form.getvalue("enquiry")
feedback = form.getvalue("subject")

print """
<!doctype html>
<html>
<head>
	<title>Thank You!</title>
</head>

<body>
<p><strong>Thank you {0} for your enquiry, we will be in touch with your desired preference {1}"</strong></p>

</body>
</html> 

""".format(name, time)
