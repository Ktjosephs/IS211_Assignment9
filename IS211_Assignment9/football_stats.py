#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Football Stats"""

from bs4 import BeautifulSoup
import urllib2


link  = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2015-season-regular-category-touchdowns'
website = urllib2.urlopen(url)
soup = BeautifulSoup(website.read())


def stats(website):
    table = soup.find_all(class_ = {'row1','row2'})
    results = '{:^20}|{:^3}|{:^4}|{:^3}'
    for row in table:
        print results.format(row.contents[0].text,row.contents[2].text,
                             row.contents[6].text)

if __name__ == '__main__':
    stats(website)
