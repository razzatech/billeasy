import json
import collections
from datetime import datetime, timedelta
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def enroll_account(input):
    response = collections.OrderedDict()
    response['success']=1
	
    if("merchant_code" in input
    and "merchant_account_number" in input
    and "custom_name" in input
    and "token"):
		#TODO: validate input here
	
        merchant_code=input["merchant_code"]
        merchant_account_number=input["merchant_account_number"]
        custom_name=input["custom_name"]
        token=input["token"]
		
        #decode token
        try:
            payload = jwt.decode(token, 'razza', algorithms=["HS256"])
            input["user_name"]=payload["user_name"]

            #connect to database
            connection=billeasy_dbconnect()
			
            add_billing_account(connection, input)
			
			
			
            response['success']=1
        except(jwt.DecodeError, jwt.ExpiredSignatureError):
            response["message"]="token invalid"

    # if response['success']:
        # #insert new user to database
        # new_user(connection, input)

        # #proceed to login: create JWT token, valid for 10 seconds
        # exp = datetime.utcnow() + timedelta(seconds=10)
        # response['name'] = given_name
        # response['token'] = jwt.encode({'user_name': user_name, 'exp': exp}, 'razza', algorithm='HS256')
        
    billeasy_dbclose(connection)
    return json.dumps(response)