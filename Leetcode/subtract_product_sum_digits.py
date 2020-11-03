
'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

'''
import numpy as np 

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = np.array([int(i) for i in str(n)])
        return np.prod(n)- np.sum(n)