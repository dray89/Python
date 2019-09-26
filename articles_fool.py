# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:21:26 2019

@author: rayde
"""
from finance_python import stock
import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html

from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url_list = []

url = "https://www.fool.ca//author//debraray//page//{0}"

for each in range(11):
    url_list.append(url.format(each))

chromedriver = "C:\\Users\\rayde\\iCloudDrive\\GitHub\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

for each in url_list:
    driver.get(each)
    saveas = ActionChains(driver).key_down(Keys.CONTROL).send_keys('S').key_up(Keys.CONTROL)
    saveas.perform()
    content = driver.page_source
    soup_page = soup(content)
    titles = soup_page.find_all('title')
    for each in titles:
        print(each.text)

class articles:
    def __general__(self, url):
        Client=urlopen(url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        return soup_page
