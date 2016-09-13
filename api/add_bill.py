import json
import collections
from datetime import datetime, timedelta
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def add_bill(input):
    response = collections.OrderedDict()
    response['success']=0
	
    if("account_id" in input
    and "bill_number" in input
    and "transaction_type" in input
    and "bill_date" in input
    and "due_date" in input
    and "beginning_balance" in input
    and "amount_due" in input
    and "amount_paid" in input
    and "ending_balance" in input
    and "token" in input):
        #decode token
        try:			
			#admin validation
            payload = jwt.decode(input["token"], 'razza', algorithms=["HS256"])
			
            if "role" in payload and payload["role"]=="admin":
			
		        #TODO: other input validation here###############################################
                response['success']=1
            else:
                response["message"]="token invalid"
        except(jwt.DecodeError, jwt.ExpiredSignatureError):
            response["message"]="token invalid"

    if response['success']:
        connection=billeasy_dbconnect()
        new_bill(connection, input)
        billeasy_dbclose(connection)

    return json.dumps(response)