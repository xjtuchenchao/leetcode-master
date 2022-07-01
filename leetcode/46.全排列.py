#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    # 1.回溯算法
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False] * len(nums)
        
        def backtrace(nums, track, used):
            if len(track) == len(nums):
                res.append(track[:])  # NOTE:注意这里需要拷贝一份！
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrace(nums, track, used)
                track.pop()
                used[i] = False
        
        backtrace(nums, track, used)
        return res
        
# @lc code=end

