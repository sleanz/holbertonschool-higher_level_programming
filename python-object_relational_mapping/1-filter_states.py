#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
Usage: python3 1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


def filter_states_n():
    """Connect to MySQL database and list all states starting with N"""
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
    
    # Execute SQL query to filter states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Display results
    for row in results:
        print(row)
    
    # Close database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states_n()
