from itertools import product
import pandas as pd
    
def perm_possible(items, repeat=5):
    perm = product(items, repeat)
    return [i for i in list(perm)]

perm = perm_possible([0,1])
