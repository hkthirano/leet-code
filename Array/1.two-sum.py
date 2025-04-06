#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums and nums.index(diff) != i:
                return [i, nums.index(diff)]
        
# @lc code=end

