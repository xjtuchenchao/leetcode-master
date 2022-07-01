'''
    给定一个非负整数，计算并返回x的算术平方根。
'''
class Solution:
    # def mySqrt(self, x):
    #     left, right = 0, x
    #     ans = -1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if mid ** 2 <= x:
    #             ans = mid
    #             left = mid + 1
    #         else:
    #             right = mid - 1   
    #     return ans   # NOTE:返回什么需要仔细琢磨!
    
    def mySqrt(self, x):
        left, right = 0, x
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1 
        return right   # NOTE:返回什么需要仔细琢磨!  如何考虑呢？首先循环结束后肯定是left>right的，假设left==right的时候，还是没有找到相等的，那么应该返回left（或者right）所对应的值，但是由于left会改变成大于right的值，所以返回right是一个选择，也可以选择返回left-1

obj = Solution()
print(obj.mySqrt(9))