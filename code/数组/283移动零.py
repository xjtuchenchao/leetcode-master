# 快慢指针：快指针指向非零元素，慢指针指向新数组下标的位置
def moveZeros(nums):
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1
        else:
            fast += 1