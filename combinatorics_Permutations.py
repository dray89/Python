# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:35:57 2020

@author: rayde

Combinatorics and permutations make me feel... [inadequate. ] like I need to study more. ;)
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


import numpy as np

C = dict()  # C[n,k] is equal to n choose k
output = []

for n in range(33):
    C[n, 0] = 1
    C[n, n] = 1

    for k in range(1, n):
        C[n, k] = C[n - 1, k - 1] + C[n - 1, k]
        output.append(C[n, k])
print(np.sum(output))

print(C[5, 3] + C[5, 4] + C[5, 5])

for n in range(6):
    [2 ** n for n in range(6)]

# Permutations(ordered, with repetitions)
# Just Tuples n**k
from itertools import product

for c in product("abc", repeat=2):
    print("".join(c))

# Permutations(ordered, without repetitions)
from itertools import permutations

for c in permutations("abc", 2):
    print("".join(c))

# Combinations (Unordered without repetitions)
from itertools import combinations

for c in combinations("abcd", 9):
    print("".join(c))

# Combinations (Unordered with repetitions)
from itertools import combinations_with_replacement

for c in combinations_with_replacement("abc", 2):
    print("".join(c))

# Fixed Sum of Digits
import itertools as it

count = 0
for d in it.product(range(10), repeat=4):
    if sum(d) == 10:
        count += 1
print(count)

from itertools import combinations

output = []
for a in combinations(["A1 ", "A2 ", "A3 ", "A4 ", "A5 ", "A6 ", "A7 ", "A8 "], 3):
    for b in combinations(["B1 ", "B2 ", "B3 ", "B4 ", "B5 "], 2):
        c = a + b
        output.append(c)
print(len(output))