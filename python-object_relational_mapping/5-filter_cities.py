#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa
Usage: python3 5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys


def filter_cities():
    """Connect to MySQL database and list cities of a specific state"""
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
    
    # Execute SQL query with JOIN and parameterized query (safe from SQL injection)
    cursor.execute("""
        SELECT cities.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        WHERE states.name = %s 
        ORDER BY cities.id ASC
    """, (state_name,))
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Display results as comma-separated values
    city_names = []
    for row in results:
        city_names.append(row[0])
    
    print(", ".join(city_names))
    
    # Close database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
