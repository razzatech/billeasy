import json
import collections
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def fetch_billing_accounts(input):
    response = collections.OrderedDict()
    response['success']=0
    
    if 'token' in input:
        token = input['token']

        try:
            #decode token
            payload = jwt.decode(token, 'razza', algorithms=["HS256"])
            user_name=payload["user_name"]
			
            response['success']=1
            response["accounts"]=[]
				
            #query database for merchant info
            connection=billeasy_dbconnect()

            if "role" in payload and payload["role"]=="admin":		
                for row in all_billing_accounts_fromdb(connection):
                    billing_account = collections.OrderedDict()
                    billing_account['account_id']=str(row["account_id"])
                    response["accounts"].append(billing_account)
            else:
                for row in billing_accounts_fromdb(connection, user_name):
                    billing_account = collections.OrderedDict()
                    billing_account['merchant_name']=row["short_name"]
                    billing_account['merchant_account_number']=row["merchant_account_number"]
                    billing_account['custom_name']=row["custom_name"]
                    billing_account['due_date']=str(row["due_date"])
                    billing_account['last_bill_date']=str(row["last_bill_date"])
                    billing_account['current_balance']=str(row["current_balance"])
                    billing_account['last_due_date']=str(row["last_due_date"])
                    billing_account['active']=str(row["active"])
                    response["accounts"].append(billing_account)
					
        except(jwt.DecodeError, jwt.ExpiredSignatureError):
            response["message"]="token invalid"
    else:
        response["message"]="malformed request"

    return json.dumps(response)