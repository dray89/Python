# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 04:35:21 2019

@author: rayde
"""
import numpy as np
import pandas as pd

class pandas_methods:
    def column_strings(self, df, string):
        '''remove strings from columns'''
        if len(df)>1:
            for each in list(df.columns):
                df[each] = df[each].str.strip(string)
        return df

    def row_strings(self, df, string):
        '''remove strings from rows'''
        for i in range(0, len(df)-1):
            for e in range(0, len(list(df.iloc[i].values))):
                if string in str(list(df.iloc[i].values)[e]):
                    a = list(df.iloc[i].values)[e]
                    a = a.strip(string)
            return df

    def numeric(self, df):
        '''convert df to numeric'''
        for each in list(df.columns):
            df.fillna(np.nan).astype(float, errors='ignore')
            df[each] = pd.to_numeric(df[each], errors='coerce')
        return df

    def add_rows(self, df, dtype= float, col1 = 'Name', col2 = 'Name'):
        '''add two rows together'''
        div_r = df.T[col1][0]
        t_r = df.T[col2][0]
        if np.isnan(div_r):
            t_r = float(t_r)
        else:
            t_r = dtype(t_r) + dtype(div_r)
        return t_r

    def divide_rows(self, df, numerator='row1 index', denominator='row2 index'):
        '''divided two rows together'''
        beta = df.T[denominator][0]
        returns_adj = abs(numerator/float(beta))
        p = returns_adj
        return p

    def append_rows(self, df, values ='series', row_name= "row name", d_type = float, column_name='column name'):
        row = pd.Series({column_name:values}, name=row_name, dtype=d_type)
        df = df.append(row)
        return df
