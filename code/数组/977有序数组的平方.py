# violent method
def violent_method(nums):  # time complexity is O(n + nlogn)
    length = len(nums)
    for i in range(length):
        nums[i] *= nums[i]
    nums.sort()
    return nums

# two points
def sortedSquares(nums):  # time complexity is O(n)
    n = len(nums)
    i, j, k = 0, n-1, n-1
    ans = [-1] * n
    while i <= j:
        lm = nums[i] ** 2
        rm = nums[j] ** 2
        if lm > rm:
            ans[k] = lm
            i += 1
        else:
            ans[k] = rm
            j -= 1
        k -= 1
    return ans