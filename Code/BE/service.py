import sqlite3
import constant
import pyodbc 
import pymssql 
import json
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '34.124.141.28' 
database = 'test' 
username = 'sqlserver' 
password = 'sql' 

from datetime import date, datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def add_to_list(id,firstname,lastname):
    try:
        conn = pymssql.connect(server = '34.124.141.28' ,database = 'test' ,user = 'sqlserver' ,password = 'sql' )
        # Once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()
        # Keep the initial status as Not Started
        c.execute("insert student (id,firstname,lastname) values(%s, %s,%s)", (id,firstname,lastname))
        # We commit to save the change
        conn.commit()
        return {"id": id, "firstname": firstname, "lastname":lastname}
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_items():
    try:
        conn = pymssql.connect(server = '34.124.141.28' ,database = 'test' ,user = 'sqlserver' ,password = 'sql' )
        c = conn.cursor()
        c.execute('select * from line')
        rows = c.fetchall()
        return { "data": rows }
    except Exception as e:
        print('Error: ', e)
        return None
