#!/usr/bin/python3

"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for query in session.query(State, City).all():
        print(f'{query.name}: {(query.id)} {query.name}')
