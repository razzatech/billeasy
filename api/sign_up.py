import json
import collections
from datetime import datetime, timedelta
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def sign_up(input):
    response = collections.OrderedDict()

    #check input
    if("given_name" in input
    and "middle_name" in input
    and "surname" in input
    and "address" in input
    and "contact_number" in input
    and "email" in input
    and "user_name" in input
    and "password" in input):
        given_name=input["given_name"];
        middle_name=input["middle_name"];
        surname=input["surname"];
        address=input["address"];
        contact_number=input["contact_number"];
        email=input["email"];
        user_name=input["user_name"];
        password=input["password"];

        #connect to database
        connection=billeasy_dbconnect()

        #check database for email match
        #results=billeasy_dbquery(connection, "SELECT user_name FROM users WHERE email=%s", (email))

        if email_already_registered(connection,email):
            response['message']= "email already registered"
            response['success']=0
        elif user_name_taken(connection, user_name):
            response['message']= "user_id taken"
            response['success']=0
        else:
            response['success']=1
    else:
        response['success']=0

    if response['success']:
        #insert new user to database
        new_user(connection, input)

        #proceed to login: create JWT token, valid for 10 seconds
        exp = datetime.utcnow() + timedelta(seconds=10)
        response['name'] = given_name
        response['token'] = jwt.encode({'user_name': user_name, 'exp': exp}, 'razza', algorithm='HS256')
        
    billeasy_dbclose(connection)
    return json.dumps(response)