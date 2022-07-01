'''
    给定一个排序数组和一个target，在数组中寻找目标值，目标值在数组中，则返回索引值，
    不在的话返回需要插入位置的下标。
'''
def violenr_search(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
    # return right + 1  # TODO:return left和return right + 1有什么联系和区别？
'''
    这里做一个分析，由于一共存在四种情况；
    1.target不在数组中，且小于第一个元素，即需要插入到数组中的最开始的位置。
    此时left还是0，而right经过while循环后其实已经变成了left-1，因此两者是等价的。
    2.target在数组中，则在while循环中就已经返回了，不会运行到第二个return。
    3.target不在数组中，但需要插入到数组中间。其实这种情况和第一种是一样的，left和right+1等价。
    4.target不在数组中，且需要插入到数组最末尾。这种情况下，right始终是len(nums)-1，
    而left经过while循环之后变成了len(nums),因此两者依然等价。
'''

def binary_search2(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

def main():
    nums = [1, 3, 5, 6]
    target = 0
    print(binary_search2(nums, target))
    
if __name__ == '__main__':
    main()