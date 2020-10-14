# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:35:57 2020

@author: rayde
"""
'''
Two ways to manually code combinatorics in python without replacement.

This isn't from leetcode, but an exercise in combinatorics from math for data science
specialization on Coursera. 
'''


n=8
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j and j < k:
                count += 1

print(count)
 
#C(n,r)=n!/(n−r)!r!

def combinatorics(n, k):
    n_list = list(range(2, n))
    n_list.reverse()
    n_factorial = n
    
    for each in n_list:
        n_factorial = n_factorial*(each)

    
    n_r  = n-k
    
    n_r_list = list(range(2, n_r))
    n_r_list.reverse()
    
    n_r_factorial = n_r
    
    for each in n_r_list:
        n_r_factorial = each*n_r_factorial
    
    k_list = list(range(2, k))
    k_list.reverse()
    k_factorial = k
    
    for each in k_list:
        k_factorial = k_factorial*(each)
    
    return n_factorial/(n_r_factorial*k_factorial)