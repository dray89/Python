# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:21:26 2019

@author: rayde
"""
from finance_python import stock
import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from lxml import html

from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url_list = []

hdrs = {"authority": "www.fool.ca",
        "method": "GET",
        "path": "/author/debraray/",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "cookie": "__cfduid=d86f29d8880747c6d2d3b6723cedcfad81569971215; __cfduid=d22208f3b20cf30aa1b4a16244774c2221569971216; _omappvp=76nUqvjKKkU9vCj1ZY56ayVqq9nYoFEmPQ1zk7ZtVXso7pP7Vlch9AUePR5jUpjvjJqtaVtAv5C93e9RTRiHhs0HXofoGVqR; dmxRegion=false; _ga=GA1.2.1944901785.1569971218; _gid=GA1.2.1425954586.1569971218; _gcl_au=1.1.1354352399.1569971218; _sp_ses.6a5e=*; seerses=e; seerses=e; seerid=114950.45913437422; seerid=114950.45913437422; _fbp=fb.1.1569971218862.408727281; fivs=%7B%22sessionFirstArticleAuthor%22%3A%22Debra%20Ray%22%2C%22sessionFirstArticlePublishDate%22%3A%222019%2010%2001%22%2C%22sessionFirstArticleUrl%22%3A%22www.fool.ca%2F2019%2F10%2F01%2Fthis-canadian-electric-bus-stock-pays-6-1-dividends%2F%22%2C%22sessionFirstArticleTitle%22%3A%22This%20Canadian%20Electric%20Bus%20Stock%20Pays%206.1%25%20Dividends%22%2C%22sessionFirstIndustryTerms%22%3A%22Automobiles%2CEnergy%22%7D; cto_lwid=8da5dae0-cad5-4920-a8b4-9be30753085e; trc_cookie_storage=taboola%2520global%253Auser-id%3D2bb0dfac-c599-4a4a-a7be-8f5ecfe7675c-tuct48d6190; __gads=ID=f51b3c5474a4d05d:T=1569971226:S=ALNI_MZiw7NFgaw4elwAQV0fPQ0_8yCAGw; wordpress_test_cookie=WP+Cookie+check; ly_segs=%7B%22smt_new%22%3A%22smt_new%22%2C%22all%22%3A%22all%22%7D; PHPSESSID=71f4b54d3c07077008f0699f0b931429; wordpress_sec_c0872e40c45a4ffdf4bfb1af4e0a4043=debraray%7C1570146119%7CBktUtoLYOtfWDBUmqwcvwEn7865jTtPEW0VgrW2hJq3%7Caca1517f09085492babdac73c49de828da10dd8bda3d7b709f861336fd21246b; wordpress_logged_in_c0872e40c45a4ffdf4bfb1af4e0a4043=debraray%7C1570146119%7CBktUtoLYOtfWDBUmqwcvwEn7865jTtPEW0VgrW2hJq3%7C0043896d69469884f6e308f4609fde67557fce98acd6562471a2485841047a90; Ookie=-1; wp-settings-56219=editor_plain_text_paste_warning%3D2%26editor%3Dtinymce%26libraryContent%3Dbrowse%26post_dfw%3Don; wp-settings-time-56219=1569973320; fivp=%7B%22userGuid%22%3A%220470e1f2-f03d-4e69-bc95-fd7c20b53e2b%22%2C%22userUid%22%3A%222045318903%22%2C%22userOwnsStockAdvisor%22%3Afalse%2C%22userOwnsPro%22%3Afalse%2C%22userIsBuyer%22%3Afalse%2C%22userIsEcapped%22%3Atrue%2C%22userOwnsDividendInvestor%22%3Afalse%2C%22userOwnsDiscovery%22%3Afalse%2C%22userOwnsDiscoveryVip%22%3Afalse%2C%22userOwnsArtificialIntelligence%22%3Afalse%2C%22userOwnsCryptoBlueprint%22%3Afalse%2C%22userOwnsHiddenGems%22%3Afalse%2C%22userOwnsMasterPass%22%3Afalse%2C%22userOwnsRecessionProtection%22%3Afalse%2C%22userAccountGuid%22%3A%2294885c49-ba12-4c89-affb-721847b2480c%22%2C%22userOwnsResourceExplorer%22%3Afalse%2C%22userOwnsResourceExplorerVip%22%3Afalse%2C%22userOwnsMarijuanaMasters%22%3Afalse%2C%22userOwnsPartnershipPortfolio%22%3Afalse%2C%22userOwnsAgeOfMiracles%22%3Afalse%2C%22userOwnsDiscoveryCa%22%3Afalse%2C%22userOwnsExtremeOpportunities%22%3Afalse%2C%22userOwnsIpoTrailblazers%22%3Afalse%7D; fool_subinfo={'username':'debraray','subscriptions':[]}; _gat=1; _gat_UA-131721307-1=1; _sp_id.6a5e=17cb470d02681dec.1569971219.1.1569973429.1569971219; PathforaPageView=21",
        "dnt": 1,
        "pragma": "no-cache",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": 1,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

url = "https://www.fool.ca/author/debraray/"


def scrape(self):
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
        soup_page = soup(content, 'html')
        titles = soup_page.find_all('title')
        for each in titles:
            print(each.text)

def general(url, hdrs):
    req = Request(url, headers=hdrs)
    Client=urlopen(req)
    xml_page=Client.read()
    Client.close()
    soup_page=soup(xml_page,"lxml")
    return soup_page
