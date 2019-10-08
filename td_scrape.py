# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:36:51 2019

@author: rayde
"""
import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html
import re
from finance_python.scrapers import scraper

class dividend_calendar:
    def __init__(self):
        pass

    def scraper(self):
        hdrs = {'Accept': 'application/json, text/plain, */*',
               'DNT': 1,
               'Origin': 'https://www.nasdaq.com',
               'Referer': 'https://www.nasdaq.com/market-activity/dividends?date=2019-Oct-09',
               'Sec-Fetch-Mode': 'cors',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        url = "https://api.nasdaq.com/api/calendar/dividends?date=2019-10-07"
        page = scraper().__general__(url, hdrs)
        page = page.extract()
        x = page.p.extract()
        sp = x.text.split('}')
        f = list(map(lambda each: re.findall(r'[a-zA-Z]+', each), sp))
        return f

    def all_methods(self):
        url = self.urls()
        for item1, item2 in url:
            filename = 'C:\\Users\\rayde\\Downloads\\{0}'.format(item1)
            con = self.content(filename)
            clean = self.clean_html(con)
            write = self.write_list(filename, clean)
        return write

    def urls():
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            "S", 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
        urls = []
    
        for each in alphabet:
            u = "https://invest.ameritrade.com/cgi-bin/apps/u/MarginReq?pagehandler=PHMarginRequirements&filter={0}".format(each)
            urls.append(u)
            urls = list(zip(alphabet, urls))
        return urls
    
    def xpath(number = 27):
        page = range(number)
        xpath_list = []
        for i in page:
            th = "/html/body/div[3]/p[2]/table[1]/tbody/tr[{0}] \n".format(i)
            xpath_list.append(th)
        return xpath_list
    
    def readurl(url, html_filename):
        response = requests.get(url, html_filename)
        return response
    
    def content(html_file = "C:\\Users\\rayde\\Downloads\\TDAmeritrade.html"):
        html_file = html_file + '.html'
        f = open(html_file, 'r+')
        content = f.read()
        return content
    
    def clean_html(contents, rex = "[<td>].*[</td>]"):
        clean_list = re.findall(rex, contents)
        return clean_list
    
    def write_list(filename, clean_list, letter = '[A-Z]+'):
        filename = filename + '.txt'
        with open(filename, 'a+') as file:
            for item in clean_list:
                y = re.findall(letter, item)
                if len(y)>0:
                    y.append('\n')
                    a = " "
                    y = a.join(y)
                    file.writelines(y)
