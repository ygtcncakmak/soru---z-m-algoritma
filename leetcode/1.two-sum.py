#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sonuc = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (nums[i]+nums[j]) == target:
                    sonuc.append(i)

                    break
        print(list(sonuc))
# @lc code=end
nums = [2, 7, 11, 15]
target=9
Solution.twoSum(nums,target)
