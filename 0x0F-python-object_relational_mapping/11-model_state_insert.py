#!/usr/bin/python3

"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    query = session.query(State).filter(State.name == 'Louisiana').first()
    if query is None:
        print('Not found')
    else:
        print(query.id)
