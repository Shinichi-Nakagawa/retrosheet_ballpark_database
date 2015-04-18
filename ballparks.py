#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

import json
import urllib.request
from bs4 import BeautifulSoup
from configparser import ConfigParser
from geopy.geocoders import Nominatim


class BallParks(object):

    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")
        html = urllib.request.urlopen(config["BallParks"]["url"])
        self.soup = BeautifulSoup(html)
        self.geolocator = Nominatim()

    def _geocode(self, name):
        """
        Geocoding
        :param name: park name
        :return: lon, lat
        """
        location = self.geolocator.geocode(name, timeout=600)
        if location is not None:
            return location.longitude, location.latitude
        else:
            return 0.0, 0.0

    def _get_parkid(self, href):
        """
        URLからparkidを取得
        :param href: url text
        :return: parkid
        """
        # urlを"_"で分けて後ろの方をGet
        params = href.split("_")
        return params[1].replace(".htm", "")

    def list(self):
        """
        球場リストをGet
        :return:
        """
        parklist = []
        for a in self.soup.find_all("a"):
            href = a.get("href")
            # 「PK_」を含むURLがある場合は球場を示す（らしい）
            if "PK_" in href:
                print(a.text)
                lon, lat = self._geocode(a.text)
                parklist.append(
                    {
                        "name": a.text,
                        "url": href,
                        "parkid": self._get_parkid(href),
                        "lon": lon,
                        "lat": lat,
                    }
                )
        return parklist


if __name__ == '__main__':
    ba = BallParks()
    with open('parklist.json', 'w') as outfile:
        json.dump(ba.list(), outfile, indent=4, sort_keys=True)
