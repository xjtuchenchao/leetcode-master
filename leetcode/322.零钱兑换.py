#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    # 1.暴力递归
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     return self.dp(coins, amount)
    
    # def dp(self, coins, amount):
    #     # base case
    #     if amount == 0:
    #         return 0
    #     if amount < 0:
    #         return -1
        
    #     res = float('inf')
    #     for coin in coins:
    #         subProblem = self.dp(coins, amount-coin)
    #         if subProblem == -1:
    #             continue
    #         res = min(res, subProblem+1)
    #     return -1 if res == float('inf') else res
    
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # base case
    #     if amount == 0:
    #         return 0
    #     if amount < 0:
    #         return -1
        
    #     res = float('inf')
    #     for coin in coins:
    #         subProblem = self.coinChange(coins, amount-coin)
    #         if subProblem == -1:
    #             continue
    #         res = min(res, subProblem+1)
    #     return -1 if res == float('inf') else res 
    
    # 2.带备忘录的递归
    # def coinChange(self, coins, amount):
    #     memo = [-666] * (amount + 1)
    #     return self.dp(coins, amount, memo)
    
    # def dp(self, coins, amount, memo):
    #     if amount == 0:
    #         return 0
    #     if amount < 0:
    #         return -1
    #     if memo[amount] != -666:
    #         return memo[amount]
    #     res = float('inf')
    #     for coin in coins:
    #         subProblem = self.dp(coins, amount-coin, memo)
    #         if subProblem == -1:
    #             continue
    #         res = min(res, subProblem+1)
    #     memo[amount] = -1 if res == float('inf') else res
    #     return memo[amount]
    
    # 3.dp数组的迭代解法
    def coinChange(self, coins, amount):
        if amount < 0:
            return -1
        dp = [amount+1] * (amount + 1)
        # base case
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i-coin])
        return -1 if dp[amount] == amount+1 else dp[amount]



        
# @lc code=end

