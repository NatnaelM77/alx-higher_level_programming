#!/usr/bin/python3

"""
lists all State objects from the database hbtn_0e_6_usa.
"""

import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id.asc()):
        print(state.id, end='')
        print(': ', end='')
        print(state.name)
