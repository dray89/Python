def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, num in enumerate(nums):
        difference = target - nums[i]
        for i2, num2 in enumerate(nums[:i:]):
            if num2==difference:
                return [i, i2]
            else:
                continue

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        for i, num in enumerate(nums):
            potentialMatch = target - num
            if potentialMatch in nums_hash:
                return [nums_hash[potentialMatch], i]
            nums_hash[num] = i
            
