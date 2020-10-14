# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:32:29 2020

@author: rayde
"""
'''
High school students asked me to help them filter stock screening results by an approved list
of stocks to use for a competition. This is the code I sent them.

'''
import pandas as pd 
#screening results
screening_results = pd.from_excel('path to file')
# approved stock list
approved_stocklist = pd.from_excel('path to file')

merged = screening_results.merge(approved_stocklist, on='symbol', how='left', indicator=True)

merged.to_excel('path to file')

