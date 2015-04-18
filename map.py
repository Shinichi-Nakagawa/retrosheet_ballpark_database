#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Park, Base

from bottle import route, run, template
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


MAP_API_KEY=config["google"]["api_key"]
MAP_CENTER = {
    'lat': 37.751526,
    'lng': -122.200470,
}


def get_session():
    engine = create_engine('sqlite:///ballpark.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


@route('/')
def index():
    session = get_session()
    return template(
        'map',
        map_key=MAP_API_KEY,
        sensor='false',
        center_lat=MAP_CENTER['lat'],
        center_lon=MAP_CENTER['lng'],
        parks=list(session.query(Park).all())
    )


if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True, reloader=True)
