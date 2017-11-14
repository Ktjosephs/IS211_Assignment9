#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Weather"""

import urllib2
from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/history/airport/KNYC/2016/2/10/MonthlyHistory.html'
html = urllib2.urlopen(url)


def weather():
    soup = BeautifulSoup(html.read())

if __name__ == '__main__':
    weather()
