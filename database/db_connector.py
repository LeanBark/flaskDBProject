import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

host = os.environ.get("cs_361projectHOST")
user = os.environ.get("cs_361projectUSER")
passwd = os.environ.get("cs_361projectPW")
db = os.environ.get("cs_361project")

def connect_to_database(host=host, user=user, passwd=passwd, db=db):
    db_connection = MySQLdb.connect(host,user,passwd, db)
    return db_connection

def execute_query(db_connection=None, query=None, query_params=()):
    if db_connection is None:
        print("No connection to database made")
        return None
    
    if query is None or len(query.strip()) == 0:
        print("query is empty")
        return None
    
    print("Executing %s with %s" % (query, query_params))

    cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

    
    cursor.execute(query, query_params)
    db_connection.commit();
    return cursor

if __name__ == "__main__":
    # sample testing for connection
    print("Executing sample query to db using credentials from db_credentials")
    query = "SELECT * FROM Restaurants"
    results = execute_query(db, query);
    print("Printing results of %s % query")

    for r in results.fetchall():
        print(r)
