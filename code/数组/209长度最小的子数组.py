# violent method
def violent_method(nums, target):
    result = 1e6
    n = len(nums)
    subLen = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum >= target:
                subLen = j - i + 1
                result = min(result, subLen)
                break
    return result if result != 1e6 else 0

# 滑动窗口
def minSubArrayLen(target, nums):
    result = 1e6
    sum = 0
    i = 0
    subLen = 0
    for j in range(len(nums)):
        sum += nums[j]
        while sum >= target:  # NOTE:不要以为for里放一个while循环就以为是O(n^2)，主要看每一个元素被操作的次数，每个元素在滑动窗口后进来操作一次，出去操作一次，每个元素被操作两次，所以时间复杂度是O(2n)->O(n)
            subLen = j - i + 1
            result = min(result, subLen)
            sum -= nums[i]
            i += 1
    return result if result != 1e6 else 0

class Solution:
    def minSubArrayLen(self, target, nums):
        result = float('inf')
        sum = 0
        index = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                result = min(result, i-index+1)
                sum -= nums[index]
                index += 1
        return 0 if result == float('inf') else result

# 前缀和 + 二分查找
class Solution:
    def minSubArrayLen(self, target, nums):
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sum.append(sum[-1] + nums[i])
        
        def binary_search(sums, target):
            left, right = 0, len(sums) - 1
            while left <= right:
                mid = (left + right) // 2
                if sums[mid] == target:
                    return mid
                elif sums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
                
        for i in range(1, n+1):
            s = target + sums[i-1]
            index = binary_search(sums, s)
            if index != len(sums):
                ans = min(ans, index-i+1)
        return 0 if ans == n+1 else ans