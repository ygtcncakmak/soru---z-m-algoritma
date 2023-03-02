#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start

class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    result=[i,j]
                    return list(result)
                    break
            if nums[i]+nums[j] == target:
                break

# @lc code=end
nums = [2,7,11,15]
target=18
Solution.twoSum(nums,target)