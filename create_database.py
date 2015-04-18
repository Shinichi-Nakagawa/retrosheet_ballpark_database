#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Park, Base


def get_session():
    engine = create_engine('sqlite:///ballpark.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def main(parklist):
    session = get_session()

    parks = []
    for park in parklist:
        parks.append(
            Park(
                parkid=park.get('parkid'),
                name=park.get('name'),
                url=park.get('url'),
                lat=park.get('lat'),
                lon=park.get('lon'),
            )
        )
    session.add_all(parks)
    session.commit()


if __name__ == '__main__':
    with open('parklist.json', 'r') as infile:
        main(json.load(infile))