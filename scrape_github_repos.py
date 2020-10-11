# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:15:38 2019
@author: rayde

Get links for github repos
"""


url = 'https://github.com/dray89?utf8=%E2%9C%93&tab=repositories&q=&type=fork&language='
soup_page = scraper(symbol).__general__(url)
a = soup_page.find_all('a', class_="muted-link mr-3")
a[0]['href']

for each in a:
    print(each['href'])
