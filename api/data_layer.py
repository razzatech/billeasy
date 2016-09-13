import sys

#non-installed module imports
sys.path.append('modules')
import pymysql

#generic db operations
def billeasy_dbconnect():
    return pymysql.connect(host="localhost", user="i1x2k4v6_admin", passwd="razzaaaa", db="i1x2k4v6_billeasy")

def billeasy_cursor(connection):
    return connection.cursor(pymysql.cursors.DictCursor)

def billeasy_dbquery(connection, query_string, params):
    cursor=billeasy_cursor(connection)
    cursor.execute(query_string, params)
    return cursor.fetchall()
    cursor.close()
	
def billeasy_dbcommit(connection):
    connection.commit()
	
def billeasy_dbclose(connection):
    connection.close()

#billeasy db operations

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

def get_email(connection, user_name_or_email):
    QUERY="SELECT email FROM users WHERE (user_name=%s OR email=%s)"
    results=billeasy_dbquery(connection, QUERY, (user_name_or_email, user_name_or_email))
    return results
    
def is_admin(connection, user_name):
    QUERY="SELECT role FROM user_roles WHERE user_name=%s"
    results=billeasy_dbquery(connection, QUERY, (user_name))
    for row in results:
        if row['role']=="admin":
            return 1
    return 0
	
def reset_password(connection, email, new_password):
    QUERY="UPDATE users SET password=%s WHERE email=%s"
    results=billeasy_dbquery(connection, QUERY, (new_password, email))
    connection.commit()

def add_billing_account(connection, input):
    INSERT="INSERT INTO billing_accounts (user_name, merchant_code, merchant_account_number, custom_name, current_balance, active)" 
    VALUES=" VALUES (%s, %s, %s, %s, 0, 1)"
    billeasy_dbquery(connection, INSERT+VALUES, (input["user_name"], input["merchant_code"], input["merchant_account_number"], input["custom_name"]))
    connection.commit()

def merchants_fromdb(connection):
    QUERY="SELECT * FROM merchants"
    return billeasy_dbquery(connection, QUERY, ())

def all_billing_accounts_fromdb(connection):
    QUERY="SELECT * FROM billing_accounts"
    return billeasy_dbquery(connection, QUERY, ())
	
def billing_accounts_fromdb(connection, user_name):
    SELECT = "SELECT merchants.short_name, "
    SELECT += "billing_accounts.merchant_account_number, "
    SELECT += "billing_accounts.custom_name, "
    SELECT += "billing_accounts.due_date, "
    SELECT += "billing_accounts.last_bill_date, "
    SELECT += "billing_accounts.current_balance, "
    SELECT += "billing_accounts.last_due_date, "
    SELECT += "billing_accounts.active FROM billing_accounts "
    JOIN= "JOIN merchants ON merchants.merchant_code = billing_accounts.merchant_code "
    WHERE = "WHERE user_name=%s"
    return billeasy_dbquery(connection, SELECT+JOIN+WHERE, (user_name))

def all_bills_fromdb(connection):
    QUERY="SELECT * FROM bills"
    return billeasy_dbquery(connection, QUERY, ())

def user_bills_fromdb(connection, user_name):
    SELECT = "SELECT bills.bill_id, " 
    SELECT += "merchants.short_name, "
    SELECT += "bills.merchant_bill_number, "
    SELECT += "bills.transaction_type, "
    SELECT += "bills.bill_date, "
    SELECT += "bills.due_date, "
    SELECT += "FORMAT(bills.beginning_balance,2), "
    SELECT += "FORMAT(bills.amount_due,2), "
    SELECT += "FORMAT(bills.amount_paid,2), "
    SELECT += "FORMAT(bills.ending_balance,2) FROM bills "
    JOIN = "JOIN billing_accounts ON bills.account_id = billing_accounts.account_id"
    JOIN += " JOIN users ON users.user_name = billing_accounts.user_name "
    JOIN += " JOIN merchants ON merchants.merchant_code = billing_accounts.merchant_code "
    WHERE= "WHERE users.user_name = %s"
    return billeasy_dbquery(connection, SELECT + JOIN + WHERE, (user_name))

def new_merchant(connection, input):
    INSERT="INSERT INTO merchants (merchant_code, short_name, full_name, contact_person, contact_number, email, address, active)" 
    VALUES=" VALUES (%s, %s, %s, %s, %s, %s, %s, 1)"
    billeasy_dbquery(connection, INSERT+VALUES, (input["merchant_code"], input["short_name"], input["full_name"], input["contact_person"], input["contact_number"], input["email"], input["address"]))
    connection.commit()

def new_bill(connection, input):
    INSERT="INSERT INTO bills (account_id, merchant_bill_number, transaction_type, bill_date, due_date, beginning_balance, amount_due, amount_paid, ending_balance)" 
    VALUES=" VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    billeasy_dbquery(connection, INSERT+VALUES, (input["account_id"], input["bill_number"], input["transaction_type"], input["bill_date"], input["due_date"], input["beginning_balance"], input["amount_due"], input["amount_paid"], input["ending_balance"]))

    UPDATE="UPDATE billing_accounts	SET last_due_date=%s, last_bill_date=%s, current_balance=%s"
    WHERE = "WHERE account_id=%s"
    billeasy_dbquery(connection, UPDATE + WHERE, (input["due_date"], input["bill_date"], input["ending_balance"], input["account_id"]))
	
    connection.commit()
	
def new_bills(connection, input):
    INSERT="INSERT INTO bills (account_id, merchant_bill_number, transaction_type, bill_date, due_date, beginning_balance, amount_due, amount_paid, ending_balance)" 
    VALUES=" VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    billeasy_dbquery(connection, INSERT+VALUES, (input["account_id"], input["bill_number"], input["transaction_type"], input["bill_date"], input["due_date"], input["beginning_balance"], input["amount_due"], input["amount_paid"], input["ending_balance"]))

    UPDATE="UPDATE billing_accounts	SET last_due_date=%s, last_bill_date=%s, current_balance=%s"
    WHERE = "WHERE account_id=%s"
    billeasy_dbquery(connection, UPDATE + WHERE, (input["due_date"], input["bill_date"], input["ending_balance"], input["account_id"]))