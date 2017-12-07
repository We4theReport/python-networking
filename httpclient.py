from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters
parms = {'name1' : 'value1', 'name2' : 'value2'}

# Encode the query string, use urllib.urlencode module
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = u.read()


