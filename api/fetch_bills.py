import json
import collections
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def fetch_bills(input):
    response = collections.OrderedDict()
    response['success']=0
    
    if 'token' in input:
        try:
            #decode token
            payload = jwt.decode(input['token'], 'razza', algorithms=["HS256"])
            response['success']=1
            response["bills"]=[]
			
            connection=billeasy_dbconnect()

            if "role" in payload and payload["role"]=="admin":
                for row in all_bills_fromdb(connection):
                    bill = collections.OrderedDict()
                    bill['bill_id']=row["bill_id"]
                    bill['account_id']=row["account_id"]
                    bill['merchant_bill_number']=row["merchant_bill_number"]
                    bill['transaction_type']=row["transaction_type"]
                    bill['bill_date']=str(row["bill_date"])
                    bill['due_date']=str(row["due_date"])
                    bill['beginning_balance']=str(row["beginning_balance"])
                    bill['amount_due']=str(row["amount_due"])
                    bill['amount_paid']=str(row["amount_paid"])
                    bill['ending_balance']=str(row["ending_balance"])
                    response["bills"].append(bill)
            elif "user_name" in payload:
                for row in user_bills_fromdb(connection, payload["user_name"]):
                    bill = collections.OrderedDict()
                    bill['bill_id']=row["bill_id"]
                    bill['merchant_name']=row["short_name"]
                    bill['merchant_bill_number']=row["merchant_bill_number"]
                    bill['bill_date']=str(row["bill_date"])
                    bill['due_date']=str(row["due_date"])
                    bill['beginning_balance']=str(row["FORMAT(bills.beginning_balance,2)"])
                    bill['amount_due']=str(row["FORMAT(bills.amount_due,2)"])
                    bill['amount_paid']=str(row["FORMAT(bills.amount_paid,2)"])
                    bill['ending_balance']=str(row["FORMAT(bills.ending_balance,2)"])
                    response["bills"].append(bill)
            billeasy_dbclose(connection)
        except(jwt.DecodeError, jwt.ExpiredSignatureError):
            response["message"]="token invalid"
    else:
        response["message"]="malformed request"        	

    return json.dumps(response)