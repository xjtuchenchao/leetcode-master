#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    # 1.暴力递归
    # def fib(self, n: int) -> int:
    #     if n <= 1:
    #         return n
    #     return self.fib(n-1) + self.fib(n-2)
    
    # 2.带备忘录的递归解法（自顶向下进行递归）
    # def fib(self, n):
    #     memo = [0] * (n+1)  # 事实上，这里完全不需要用到memo[1],因为n=1的情况可以直接返回值了。
    #     return self.helper(memo, n)
    
    # def helper(self, memo, n):
    #     if n <= 1:
    #         return n
    #     if memo[n] != 0:
    #         return memo[n]
    #     memo[n] = self.helper(memo, n-1) + self.helper(memo, n-2)
    #     return memo[n]
    
    # 3.dp数组的迭代（递推）解法
    # def fib(self, n):
    #     if n <= 1:
    #         return n
    #     dp = [0] * (n+1)
    #     # base case
    #     dp[0] = 0
    #     dp[1] = 1
    #     # 状态转移
    #     for i in range(2, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]
    
    # 4.对方法3进行空间优化：当前状态只和前两个状态有关，没有必要开这么大的一个数组（列表）。
    def fib(self, n):
        if n <= 1:
            return n
        dp_i_1 = 1
        dp_i_2 = 0
        for i in range(2, n+1):
            dp_i = dp_i_1 + dp_i_2
            dp_i_2 = dp_i_1  # NOTE:要注意这里更新的顺序！先更新较远的那个
            dp_i_1 = dp_i
            
        return dp_i_1
        
            
# @lc code=end

