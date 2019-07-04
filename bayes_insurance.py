# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 23:03:34 2019

@author: rayde

    Conditional Probability: Probabilities of Illness for various risk types
    Population Probability: Population demographic distribution
    Unconditional Expected Income: Median Population Income
    income_loss: healthy income minus sick income
    utility = represents the willingness to pay above expected health care costs.
    
"""
import pandas as pd 

'''
Define Probability Table
'''
cond_prob = [.12,.3,.6]
pop_prob = [.1,.1,.8]
joint_prob = []
marginal = []

probabilities  = {"low risk":[.12,.1], "medium risk": [.3,.1], "high risk": [.6,.8]}
insurance_table = pd.DataFrame.from_dict(probabilities, orient='index', columns = ['Conditional Probability', 'Population Probability'])

'''
Calculate Baynesian Probabilities
'''
for val in range(len(cond_prob)):
    joint_prob.append(cond_prob[val]*pop_prob[val]) 

for index in range(len(cond_prob)):
    marginal.append(cond_prob[index]*sum(joint_prob))

marginal
joint_prob
'''
expected income unconditional on risk type = median population income

'''
expected_income = 10
expected_loss = marginal*expected_income
'''
benefit as a percentage of full coverage against expected income losses
'''

benefit = [.329, .46, .506]

'''
Calculate Percent Coverage for various premium
'''
premium = [1.402028337, 1.958149706, 2.155451038]
risk_premium = premium - benefit*expected_loss

'''
Create an Insurance Table Data Frame
'''
insurance_table['Expected Income'] = expected_income
insurance_table['Yearly Premium'] = premium
