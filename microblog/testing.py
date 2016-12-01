import json,urllib, sys
from flask import render_template, flash, redirect, url_for, request

url = 'http://128.199.232.32/todo/api/v1.0/tasks'
data = urllib.urlencode({'title' : 'joe',
                         'description'  : '10'})


# make a string with the request type in it:
method = "POST"
# create a handler. you can specify different handlers here (file uploads etc)
# but we go for the default
handler = urllib.HTTPHandler()
# create an openerdirector instance
opener = urllib.build_opener(handler)
# build a request
data = urllib.urlencode(data)
request = urllib.Request(url, data=data)
# add any other information you want
request.add_header("Content-Type",'application/json')
# overload the get method function with a small anonymous function...
request.get_method = lambda: method
# try it; don't forget to catch the result
try:
    connection = opener.open(request)
except urllib2.HTTPError,e:
    connection = e

# check. Substitute with appropriate HTTP code.
if connection.code == 200:
    data = connection.read()
    # handle the error case. connection.read() will still contain data
    # if any was returned, but it probably won't be of any use