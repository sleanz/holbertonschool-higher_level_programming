#!/usr/bin/python3
"""
Script that displays all values in states table where name matches the argument
This script is safe from MySQL injections
Usage: python3 3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys


def my_safe_filter_states():
    """Connect to MySQL database and filter states by name (safe from SQL injection)"""
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
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
    
    # Execute SQL query using parameterized query (SAFE FROM SQL INJECTION)
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Display results
    for row in results:
        print(row)
    
    # Close database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
