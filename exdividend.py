# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:02:35 2019

@author: rayde
"""


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
    pandas.concat(october.calendars)