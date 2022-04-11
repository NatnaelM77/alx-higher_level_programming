#!/usr/bin/python3

""" Print all City objs from db 'hbtn_0e_14_usa' """

from sys import argv
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for query in session.query(State, City).filter(State.id ==
                                                   City.state_id):
        print(f'{query.State.name}: {(query.City.id)} {query.City.name}')
