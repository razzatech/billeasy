#!/usr/bin/python
import cgi
import cgitb
import os
import sys
import string
import collections

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def save_uploaded_file (form_field):
	#TODO: validate token##############################################	
	
    form = cgi.FieldStorage()
    if not form.has_key(form_field): return
    fileitem = form[form_field]
	
    lines=string.split(fileitem.file.read(10000000),"\n")
    connection=billeasy_dbconnect()

    for line in lines:
        rows=string.split(line,",")
		
        input=collections.OrderedDict()
        input["account_id"]=rows[0]
        input["bill_number"]=rows[1]
        input["transaction_type"]=rows[2]
        input["bill_date"]=rows[3]
        input["due_date"]=rows[4]
        input["beginning_balance"]=rows[5]
        input["amount_due"]=rows[6]
        input["amount_paid"]=rows[7]
        input["ending_balance"]=rows[8]
        new_bills(connection, input)
    billeasy_dbcommit(connection)
    billeasy_dbclose(connection)

save_uploaded_file ("file_1")

print("Location:http://billeasy.razzatech.com/#/bills_csv_uploaded\n")