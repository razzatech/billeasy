import sys

#non-installed module imports
sys.path.append('modules')
import pymysql


def billeasy_dbconnect():
    return pymysql.connect(host="localhost", user="i1x2k4v6_admin", passwd="razzaaaa", db="i1x2k4v6_billeasy")

def billeasy_cursor(connection):
    return connection.cursor(pymysql.cursors.DictCursor)

def billeasy_dbquery(connection, query_string, params):
    cursor=billeasy_cursor(connection)
    cursor.execute(query_string, params)
    return cursor.fetchall()
    cursor.close()
    
def billeasy_dbclose(connection):
    connection.close()
    
    
    

def email_already_registered(connection, email):
    results=billeasy_dbquery(connection, "SELECT user_name FROM users WHERE email=%s", (email))
    if len(results)>0:
        return 1
    else:
        return 0
        
def user_name_taken(connection, user_name):
    results=billeasy_dbquery(connection, "SELECT user_name FROM users WHERE user_name=%s", (user_name))
    if len(results)>0:
        return 1
    else:
        return 0 

def new_user(connection, input):
    INSERT="INSERT INTO users (user_name, password, last_name, first_name, middle_name, email, contact_number, address)" 
    VALUES=" VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    billeasy_dbquery(connection, INSERT+VALUES, (input["user_name"], input["password"], input["surname"], input["given_name"], input["middle_name"], input["email"], input["contact_number"], input["address"]))

    INSERT="INSERT INTO billeasy_accounts (last_name, first_name, middle_name, email, contact_number, address, user_name)" 
    VALUES=" VALUES (%s, %s, %s, %s, %s, %s, %s)"
    billeasy_dbquery(connection, INSERT+VALUES, (input["surname"], input["given_name"], input["middle_name"], input["email"], input["contact_number"], input["address"], input["user_name"]))
    
    INSERT="INSERT INTO user_roles (user_name, role, date_modified, modified_by)" 
    VALUES=" VALUES (%s, \"user\", NOW(), %s)"
    billeasy_dbquery(connection, INSERT+VALUES, (input["user_name"],input["user_name"]))
    
    connection.commit()

def authenticate(connection, user_name_or_email, password):
    QUERY="SELECT user_name, first_name FROM users WHERE (user_name=%s OR email=%s) AND password=%s"
    results=billeasy_dbquery(connection, QUERY, (user_name_or_email, user_name_or_email, password))
    return results
    