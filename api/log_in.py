import json
import collections
from datetime import datetime, timedelta
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def log_in(input):
    response = collections.OrderedDict()
    response['success']=0
    
    #check input
    if("user_name_or_email" in input and "password" in input):
        user_name_or_email=input["user_name_or_email"];
        password=input["password"];
        
        #connect to database
        connection=billeasy_dbconnect()

        results=authenticate(connection, user_name_or_email, password)

        if len(results)>0:
            user_name = results[0]["user_name"]
            
            #create JWT token, valid for 1 week
            exp = datetime.utcnow() + timedelta(seconds=10)
            response['name'] = results[0]["first_name"]
            response['token'] = jwt.encode({'user_name': user_name, 'exp': exp}, 'razza', algorithm='HS256')
            response['success']=1
            
    billeasy_dbclose(connection)        
    return json.dumps(response)