#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Usage: python3 0-select_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


def list_states():
    """Connect to MySQL database and list all states"""
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create cursor object
    cursor = db.cursor()
    
    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Display results
    for row in results:
        print(row)
    
    # Close database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
