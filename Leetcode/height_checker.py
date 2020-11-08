class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        for each in list(zip(sorted(heights), heights)):
            if each[0] != each[1]:
                count+=1
        return count
        