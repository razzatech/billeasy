import json
import collections
from datetime import datetime, timedelta
import sys
import urllib
import urllib2

#non-installed module imports
sys.path.append('modules')
import jwt

#billeasy api imports
from data_layer import *

def forgot_password(input):
    response = collections.OrderedDict()
    response['success']=0
    
    if 'user_name_or_email' in input:
        #get associated email
        connection=billeasy_dbconnect()
        results=get_email(connection, input['user_name_or_email'])

        if len(results)>0:
		
	        #write email
            url="http://billeasy.razzatech.com/api/sendmail.php"
			
            link_values={
                "token":"NhEKX6jwSPDSxVqMTLsqnzebhMVDchbPJPetFu3mEmWwLGmQTRRExdq4fLdvV8z6bQPxpNXrXeKpk7zktj7RyxZNgKxtEhk3q6CNGqDBDzKxspy5ZSVHxVUvxTCbJqy8yNKxpYs3jB8xN2LMGcT7esuqpZyuzLUv5xRTf3RxPHUU2QwaUfFpNU4Z5aGXNuYdqvfAfstyRZLCejgPZphrnHAUTnCkr42erDkyS5Nu89BQS6fF2Wv6sT5paKFQ8kqvkjwwCf9ZkDKNAWnsQGVeagZYDuuvgC6J9Bs6HEFPBBNRmawnx8DgE6xqpR3YcG7GGYsLMg3B5vWVpnasXd8CPnyWefctkeLpTUma2x6BradDV4rfrpaJHTrDyeuBa7uBcFq3beJLxDAVrTkZCvrJSShFU38ZhA4j9Yk8tLxf9VLRt23w55pBRKDjnvgZ2wQptZjL7sQ2KpMW4XR8zzed2zLkFQyTDXSCWwYe5Hag2JdxKw4SQKeNpLJHCF4ZT5EU",
                "email": results[0]["email"]
            }
            link_data = urllib.urlencode(link_values)
			
			
            values= {
                "token":"NhEKX6jwSPDSxVqMTLsqnzebhMVDchbPJPetFu3mEmWwLGmQTRRExdq4fLdvV8z6bQPxpNXrXeKpk7zktj7RyxZNgKxtEhk3q6CNGqDBDzKxspy5ZSVHxVUvxTCbJqy8yNKxpYs3jB8xN2LMGcT7esuqpZyuzLUv5xRTf3RxPHUU2QwaUfFpNU4Z5aGXNuYdqvfAfstyRZLCejgPZphrnHAUTnCkr42erDkyS5Nu89BQS6fF2Wv6sT5paKFQ8kqvkjwwCf9ZkDKNAWnsQGVeagZYDuuvgC6J9Bs6HEFPBBNRmawnx8DgE6xqpR3YcG7GGYsLMg3B5vWVpnasXd8CPnyWefctkeLpTUma2x6BradDV4rfrpaJHTrDyeuBa7uBcFq3beJLxDAVrTkZCvrJSShFU38ZhA4j9Yk8tLxf9VLRt23w55pBRKDjnvgZ2wQptZjL7sQ2KpMW4XR8zzed2zLkFQyTDXSCWwYe5Hag2JdxKw4SQKeNpLJHCF4ZT5EU",
                "to": results[0]["email"],
                "subject":"Billeasy password reset",
                "body":"Click <a href='http://billeasy.razzatech.com/api/password_reset.py?" + link_data +"'>this link</a> to reset your Billeasy password."
            }
			
            data = urllib.urlencode(values)
		
	        #send mail via sendmail.php
            content = urllib2.urlopen(url+"?"+data)

        response['success']=1
		
        billeasy_dbclose(connection)
    else:
        response["message"]="malformed request"

    return json.dumps(response)