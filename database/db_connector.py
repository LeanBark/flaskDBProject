import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv

# checks for matching variables in .env file and stores their values into local variables
load_dotenv(find_dotenv())

host = os.environ.get("cs_361projectHOST")
user = os.environ.get("cs_361projectUSER")
passwd = os.environ.get("cs_361projectPW")
db = os.environ.get("cs_361project")

# establishes connection with database by passing these credentials to the database for authorized access
def connect_to_database(host=host, user=user, passwd=passwd, db=db):
    db_connection = MySQLdb.connect(host,user,passwd, db)
    return db_connection

# passes queries to the database if connection is successful and the queries are valid
def execute_query(db_connection=None, query=None, query_params=()):
    if db_connection is None:
        print("Failed to connect to database. Ensure your credential values are correct.")
        return None
    
    if query is None or len(query.strip()) == 0:
        print("The database did not recieve a query. Ensure you are passing valid queries.")
        return None
    
    print("Executing %s with %s" % (query, query_params))

    cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

    
    cursor.execute(query, query_params)
    db_connection.commit();
    return cursor

if __name__ == "__main__":
    # sample testing for connection and query validity
    print("Executing sample query to db using credentials from db_credentials or.env")
    query = "SELECT * FROM Restaurants"
    results = execute_query(db, query);
    print("Printing results of %s % query")

    for r in results.fetchall():
        print(r)
