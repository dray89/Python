'''

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

'''
import numpy as np

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        first = np.diagonal(mat)
        second = np.diagonal(mat[::-1])
        if len(mat)%2==0:
            answer = np.sum(first) + np.sum(second)
        elif len(mat)>1:
            answer = np.sum(first) + np.sum(second) - first[len(first)//2]
        else:
            answer = np.sum(mat)
        return answer

