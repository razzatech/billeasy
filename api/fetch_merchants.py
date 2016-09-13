import json
import collections
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def fetch_merchants(input):
    response = collections.OrderedDict()
    response['success']=0
    
    if 'token' in input:
        token = input['token']

        try:
            #decode token
            payload = jwt.decode(token, 'razza', algorithms=["HS256"])

            response['success']=1
            response["merchants"]=[]
				
            #query database for merchant info
            connection=billeasy_dbconnect()

            if "role" in payload and payload["role"]=="admin":		
                for row in merchants_fromdb(connection):
                    merchant = collections.OrderedDict()
                    merchant['merchant_code']=row["merchant_code"]
                    merchant['short_name']=row["short_name"]
                    merchant['full_name']=row["full_name"]
                    merchant['contact_person']=str(row["contact_person"])
                    merchant['contact_number']=str(row["contact_number"])
                    merchant['email']=row["email"]
                    merchant['address']=row["address"]
                    merchant['active']=row["active"]
                    response["merchants"].append(merchant)
            else:		
                for row in merchants_fromdb(connection):
                    merchant = collections.OrderedDict()
                    merchant['merchant_code']=row["merchant_code"]
                    merchant['short_name']=row["short_name"]
                    merchant['full_name']=row["full_name"]
                    response["merchants"].append(merchant)
        except(jwt.DecodeError, jwt.ExpiredSignatureError):
            response["message"]="token invalid"
    else:
        response["message"]="malformed request"

    return json.dumps(response)