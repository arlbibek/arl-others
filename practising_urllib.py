# Practicing urllib
'''
https://en.wikipedia.org/wiki/URL?key=value&life=42#History

Protocol: https
Host: en.wikipedia.org
Path: wiki/URL
Querystring: key=value&life=42
Fragment: History

# urllib module
request: Open URLs
response: (used internally by request)
error: request exceptions
parse: useful URL functions
robotparser: robots.txt files
'''
from urllib import request, parse

resp = request.urlopen("https://www.wikipedia.org/")
type(resp)
resp.code  # get response code: 200, 404, etc.
resp.length  # size of response in bytes
resp.peek()  # look at small part of the response

# read the entire response #once you read the response python closes the connection.
data = resp.read()
print(type(data))

html = data.decode("UTF-8")  # decoding binary data into text
type(html)

# use parse module to construct querystring

# dictonary containing the querystring parameters
param = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(param)
print(querystring)
