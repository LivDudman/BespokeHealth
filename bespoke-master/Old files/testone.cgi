
#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
print "Content-Type: text/html\n"
formData = cgi.FieldStorage()
title = formData.getvalue('title')
surname = formData.getvalue('surname')
print """
<!doctype html>
<html>
<head>
<title>Test CGI Script</title>
</head>
<body>
<p><strong>{0} {1}</strong>, thank you for
your inquiry. We will be in touch soon.</p>
</body>
</html>
""".format(title, surname)
