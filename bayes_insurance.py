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

'''
Calculate Baynesian Probabilities
'''
for val in range(len(cond_prob)):
    joint_prob.append(cond_prob[val]*pop_prob[val]) 

for index in range(len(cond_prob)):
    marginal.append(cond_prob[index]*sum(joint_prob))

''' 
Create Dictionary and DataFrame
'''

probabilities  = {"low risk":[cond_prob[0],pop_prob[0], joint_prob[0], marginal[0]], 
                  "medium risk": [cond_prob[1],pop_prob[1], joint_prob[1], marginal[1]], 
                  "high risk": cond_prob[2],pop_prob[2], joint_prob[2], marginal[2]}

insurance_table = pd.DataFrame.from_dict(probabilities, orient='index',
                                         columns = ['Conditional Probability', 
                                                    'Population Probability', 
                                                    'Joint Probability', 
                                                    'Marginal Probability'])
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
