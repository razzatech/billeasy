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
from sign_up import *
from log_in import *
from forgot_password import *
from fetch_billing_accounts import *
from enroll import *
from renew_token import *
from add_merchant import *
from fetch_merchants import *
from add_bill import *
from fetch_bills import *

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
elif pathinfo == '/forgot_password':
    print(forgot_password(GET_data()))
elif pathinfo == '/fetch_billing_accounts':
    print(fetch_billing_accounts(GET_data()))
elif pathinfo == '/enroll':
    print(enroll_account(POST_data()))
elif pathinfo == '/renew_token':
    print(renew_token(GET_data()))
elif pathinfo == '/add_merchant':
    print(add_merchant(POST_data()))
elif pathinfo == '/fetch_merchants':
    print(fetch_merchants(GET_data()))
elif pathinfo == '/add_bill':
    print(add_bill(POST_data()))
elif pathinfo == '/fetch_bills':
    print(fetch_bills(GET_data()))
else:
    print("wat")