#!/usr/bin/python
import cgi
import cgitb
import os
import sys
import string
import collections
import random
import json
import urllib
import urllib2

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

response = collections.OrderedDict()
response["success"]=0

#get url data
input = collections.OrderedDict()
arguments = cgi.FieldStorage()
for i in arguments.keys():
    input[i]=arguments[i].value

token="NhEKX6jwSPDSxVqMTLsqnzebhMVDchbPJPetFu3mEmWwLGmQTRRExdq4fLdvV8z6bQPxpNXrXeKpk7zktj7RyxZNgKxtEhk3q6CNGqDBDzKxspy5ZSVHxVUvxTCbJqy8yNKxpYs3jB8xN2LMGcT7esuqpZyuzLUv5xRTf3RxPHUU2QwaUfFpNU4Z5aGXNuYdqvfAfstyRZLCejgPZphrnHAUTnCkr42erDkyS5Nu89BQS6fF2Wv6sT5paKFQ8kqvkjwwCf9ZkDKNAWnsQGVeagZYDuuvgC6J9Bs6HEFPBBNRmawnx8DgE6xqpR3YcG7GGYsLMg3B5vWVpnasXd8CPnyWefctkeLpTUma2x6BradDV4rfrpaJHTrDyeuBa7uBcFq3beJLxDAVrTkZCvrJSShFU38ZhA4j9Yk8tLxf9VLRt23w55pBRKDjnvgZ2wQptZjL7sQ2KpMW4XR8zzed2zLkFQyTDXSCWwYe5Hag2JdxKw4SQKeNpLJHCF4ZT5EU"

if 'email' in input and 'token' in input and token==input['token']:
    connection=billeasy_dbconnect()
    results=get_email(connection, input['email'])
    
    if len(results)>0:
        new_password=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
		
        reset_password(connection, input['email'], new_password)
		
        #write email
        url="http://billeasy.razzatech.com/api/sendmail.php"
        values= {
            "token":token,
            "to": input['email'],
            "subject":"Your new password",
            "body":"Your new password is: "+new_password
        }
		
        data = urllib.urlencode(values)
		
		#send mail via sendmail.php
        content = urllib2.urlopen(url+"?"+data)
			
        response["success"]=1
    billeasy_dbclose(connection)

#redirect to billeasy
print("Location:http://billeasy.razzatech.com/#/password_reset\n")