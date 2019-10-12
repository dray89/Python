# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:31:25 2019

@author: rayde
"""
from finance_python import stock
import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html

class mj(stock):
    def __init__(self, weed_stocks, links):
        self.attributes = [ ]
        self.stocks = list(zip(weed_stocks, links))
        #self.soup = soup()

    def __general__(self, url):
        Client=urlopen(url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        return soup_page

    def __table__(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        table = tree.xpath('//table')
        table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
        return table

    def sales_growth(self):
        sales_growth = []
        return sales_growth

    def production_costs(self):
        cost_of_production = []
        return cost_of_production

    def cost_sold(self):
        cost_of_goods_sold = []
        return cost_of_goods_sold

    def soup(self):
        soup_page = list(map(lambda x: self.__general__(x[1]), self.stocks))
        return soup_page

    def items(self, soup_page):
        item_list = soup_page.find_all('item')
        return item_list

    def links(self, soup_page):
        links_list = soup_page.find_all('link')
        return links_list

    def titles(self, soup_page):
        titles = soup_page.find_all('title')
        return titles

    def description(self, soup_page):
        descriptions = soup_page.find_all('description')
        return descriptions

    def subject(self, soup_page):
        subject = soup_page.find_all('subject')
        return subject

if __name__ == '__main__':
    weed_stocks = ['CRON.TO', 'FIRE.TO', 'ACB.TO',
               'VFF.TO', 'APHA.TO', 'WEED.TO', 'TGOD.TO']

    links = ['https://www.globenewswire.com/RssFeed/Organization/n40N3EwqUdtaSsRfodARTg==',
                 'https://www.prnewswire.com/news-releases/supreme-cannabis-announces-q4-and-2019-fiscal-year-end-financial-results-300920109.html',
                 "https://www.prnewswire.com/news-releases/aurora-cannabis-announces-financial-results-for-the-fourth-quarter-and-2019-fiscal-year-300916447.html",
                'https://www.globenewswire.com/RssFeed/Organization/JDHyurLpImZNh2UX9_Ud2g==',
                'https://www.globenewswire.com/RssFeed/Organization/R1h25zYnVjsHP2c9g1rymw==',
                'https://www.prnewswire.com/news-releases/canopy-growth-drives-revenue-with-94-increase-in-recreational-dried-cannabis-sales-in-first-quarter-of-fiscal-2020-300901964.html',
                'https://www.globenewswire.com/RssFeed/Organization/hp_wl2JXUNsysLV7iSAl9A==']

    acb_data = [{'rev_change':.61}, {'revenue':94.6}, {'production_cost': 1.14},
                      {'volume': 29034}, {'volume_chg': .86}, {'gross margin': .58},
                      {'medical patients': 89700}]

    cgc_data = [{'rev_change': -.038}, {'revenue':90.5}, {'production_cost': },
                      {'volume': 10,549 }, {'volume_chg': .13 }, {'gross margin': .43 }]