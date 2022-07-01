#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    # 1.动态规划解法
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i])
        return res
    
    # 2.二分查找解法
    # def lengthOfLIS(self, nums):
    #     top = [-1e5] * len(nums)
    #     piles = 0
    #     for i in range(len(nums)):
    #         poker = nums[i]

    #         left, right = 0, piles
    #         while left <= right:
    #             mid = (left + right) // 2
    #             if top[mid] > poker:
    #                 right = mid - 1
    #             elif top[mid] < poker:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
            
    #         if left == piles:
    #             piles += 1
    #         top[left] = poker
    #     return piles
        
# @lc code=end

