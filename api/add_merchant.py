import json
import collections

#billeasy api imports
from data_layer import *

#TODO check token!!!!

def add_merchant(input):
    response = collections.OrderedDict()

    #check input
    if("merchant_code" in input
    and "short_name" in input
    and "full_name" in input
    and "contact_person" in input
    and "contact_number" in input
    and "email" in input
    and "address" in input):
        merchant_code=input["merchant_code"];
        short_name=input["short_name"];
        full_name=input["full_name"];
        contact_person=input["contact_person"];
        contact_number=input["contact_number"];
        email=input["email"];
        address=input["address"];

        #connect to database
        connection=billeasy_dbconnect()
		
        #TODO: check for collision
		#TODO: check token
        response['success']=1

    if response['success']:
        #insert new user to database
        new_merchant(connection, input)

    billeasy_dbclose(connection)
    return json.dumps(response)