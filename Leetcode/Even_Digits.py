'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for each in nums:
            num_digits = len(str(each))
            if num_digits % 2 ==0:
                count+=1
        return count