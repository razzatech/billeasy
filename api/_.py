#!/usr/bin/python
import cgitb
import cgi
import collections
import json
import os
import sys
from datetime import datetime, timedelta

#non-installed module imports
sys.path.append('modules')
import pymysql
import jwt

#billeasy api imports
from log_in import *
from sign_up import *
from renew_token import *

#enable debugging
cgitb.enable

def GET_data():
    output = collections.OrderedDict()
    arguments = cgi.FieldStorage()
    for i in arguments.keys():
        output[i]=arguments[i].value
    return output
    
def POST_data():
    return json.loads(cgi.FieldStorage().value)

print("Content-type: text/html\n\n")

#routing
pathinfo = os.environ.get('PATH_INFO', '')

if pathinfo == '/sign_up':   
    print(sign_up(POST_data()))
elif pathinfo == '/log_in':
    print(log_in(POST_data()))
elif pathinfo == '/renew_token':
    print(renew_token(GET_data()))
else:
    print("wat")