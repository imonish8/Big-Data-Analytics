class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0
        l = len(nums)
        for i in range(l):
            for j in range(i + 1,l):
                    sum = nums[i] + nums[j]
                    if(sum == target):
                        return (i,i+1)
                        

# https://leetcode.com/problems/two-sum/

# trick is to find a brute force approach and then go by optimasation.
