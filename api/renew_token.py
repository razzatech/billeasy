import json
import collections
from datetime import datetime, timedelta
import sys

#non-installed module imports
sys.path.append('modules')
import jwt

def renew_token(input):
    response = collections.OrderedDict()
    response['success']=0
    
    if 'token' in input:
        token = input['token']

        try:
            #decode token
            payload = jwt.decode(token, 'razza', algorithms=["HS256"])
            user_name=payload["user_name"]

            #create JWT token, valid for 10 seconds
            exp = datetime.utcnow() + timedelta(seconds=10)
            
            if "role" in payload and payload["role"]=="admin":
                response['token'] = jwt.encode({'user_name': user_name, 'role': 'admin', 'exp': exp}, 'razza', algorithm='HS256')
            else:
                response['token'] = jwt.encode({'user_name': user_name, 'exp': exp}, 'razza', algorithm='HS256')
                
            response['success']=1
        except(jwt.DecodeError, jwt.ExpiredSignatureError):
            response["message"]="token invalid"
    else:
        response["message"]="malformed request"

    return json.dumps(response)