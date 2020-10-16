# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:35:57 2020

@author: rayde
"""

'''
Get all the possible permutations for a set of objects.
'''

from itertools import product
import pandas as pd
    
def perm_possible(items, repeat=5):
    perm = product(items, repeat)
    return [i for i in list(perm)]

perm = perm_possible([0,1])



'''
Two ways to manually code combinatorics in python without replacement.

'''

#Method 1
n=8
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j and j < k:
                count += 1

print(count)
 
#Method 2
#C(n,r)=n!/(n−r)!r!

def combinatorics(n, k):
    
    # Calculate n-factorial  
    n_list = list(range(2, n))
    n_list.reverse()
    n_factorial = n
    
    for each in n_list:
        n_factorial = n_factorial*(each)

    # Calculate n minus k factorial 
    n_r  = n-k
    
    n_r_list = list(range(2, n_r))
    n_r_list.reverse()
    
    n_r_factorial = n_r
    
    for each in n_r_list:
        n_r_factorial = each*n_r_factorial
    
    # Calculate k factorial
    k_list = list(range(2, k))
    k_list.reverse()
    k_factorial = k
    
    for each in k_list:
        k_factorial = k_factorial*(each)
    
    # Plug into formula and return
    return n_factorial/(n_r_factorial*k_factorial)