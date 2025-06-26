#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
Usage: python3 4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


def cities_by_state():
    """Connect to MySQL database and list all cities with their states"""
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
    
    # Execute SQL query with JOIN to get cities and states
    cursor.execute("""
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        ORDER BY cities.id ASC
    """)
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Display results
    for row in results:
        print(row)
    
    # Close database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    cities_by_state()
