'''
    给定一个升序数组和一个目标值，找出给定目标值的起始位置和结束位置。
'''
def getRightBorder(nums, target):  # 目的是找到最右边的边界
    left, right = 0, len(nums) - 1
    rightBorder = -2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            rightBorder = left
    return rightBorder

def getLeftBorder(nums, target):  # 目的是找到最左边的边界
    left, right = 0, len(nums) - 1
    leftBorder = -2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
            leftBorder = right
        else:
            left = mid + 1
    return leftBorder

def binary_search(nums, target):
    leftBorder = getLeftBorder(nums, target)
    rightBorder = getRightBorder(nums, target)
    if leftBorder == -2 or rightBorder == -2:
        return [-1, -1]
    if rightBorder - leftBorder > 1:
        return [leftBorder+1, rightBorder-1]
    return [-1, -1]

# 解法2：
class Solution:
    def searchRange(self, nums, target):
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        index = binary_search(nums, target)
        if index == -1:
            return [-1, -1]
        left, right = index, index
        while left - 1 >= 0 and nums[left-1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right+1] == target:
            right += 1
        return [left, right]