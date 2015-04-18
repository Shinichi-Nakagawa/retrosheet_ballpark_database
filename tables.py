#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


from sqlalchemy.ext import declarative
from sqlalchemy import Column, Float, Unicode, Integer
Base = declarative.declarative_base()


class Park(Base):
    __tablename__ = 'park'
    id = Column(Integer, primary_key=True, autoincrement=True)
    parkid = Column(Unicode(6))
    name = Column(Unicode(255))
    url = Column(Unicode(255))
    lat = Column(Float)
    lon = Column(Float)

    def __repr__(self):
        return "<Park(PARKID={parkid}, name={name}, lat={lat}, lon={lon})>".format(
            parkid=self.parkid,
            name=self.name,
            lat=self.lat,
            lon=self.lon
        )
