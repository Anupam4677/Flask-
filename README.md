# Flask-

# http Request 
## any request contains 3 things 
## request or start line  - 
## header 
## body(optional)

# Response Status code
## 2xx -ok
## 3xx- redirect(e.g 302)
## 4xx - client error(e.g 404 URI not found)
## 5xx - server errors(e.g 505 http version not supported)

# parameters of get request are embedded in the URL 
# IN GET Request the URL has max length limit 
# data can be cached or bookmarked in browser
# dont cahnge the state of the server 

# parameters for POST request are embedded in the body - sensitive information 
# no max limit for length 
# not cached or bookmarked
# change the state of the server - can post , delete, update data 

# Routing 
# www.abc.com/?greeting=hello -part after / is called a query string-GET parameters
# get parameters can be included in url as above 
# its in form of key value pair - key = greetings , value = hello
# Request object 
# 1. context variable 
# 2. holds the GET request details
# 3. python dectionary wit key-value pair

# strings_ numbers and float

