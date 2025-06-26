#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
Usage: python3 7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_all_states():
    """List all State objects from the database"""
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all states ordered by id
    states = session.query(State).order_by(State.id).all()
    
    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    # Close session
    session.close()


if __name__ == "__main__":
    fetch_all_states()
