# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:03:46 2019
@author: rayde
"""
from finance_python=import dividend_calendar
import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html
import re, json

class dividend_calendar:

    calendars = []

    def __init__(self):
        self.attributes = 'scraper(self, year, month, day), calendar(self, dictionary = output from scraper)'

    def scraper(self, url, hdrs):
	s = requests.Session() 
        page = s.get(url, params = hdrs)
        page = page.content
        dictionary = json.loads(page)
        return dictionary

    def calendar(self):
        '''
        Returns a JSON dictionary with keys (data, message, status) 
        Next Level: dictionary['data'].keys() => calendar, timeframe
        dictionary['data']['calendar'].keys() => headers, rows
        dictionary['data']['calendar']['headers'] => column names
        dictionary['data']['calendar']['rows'] => returns list of dicts
        '''
        hdrs =
        url =
        dictionary = scraper()
        rows = dictionary['data']['calendar']['rows']
        calendar = pandas.DataFrame(rows)
        calendar = calendar.set_index('companyName')
        self.calendars.append(calendar)
        return calendar

    def quote(self, symbol):


if __name__ == '__main__':
    year = '2019'
    month = '10'
    day = list(range(31))
    october = dividend_calendar()
    for each in day:
        try:
            dictionary = october.scraper(year, month, str(each))
            october.calendar(dictionary)
        except:
            pass
    october.calendars
    df = pandas.concat(october.calendars)