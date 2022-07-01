def removeDuplicates(nums):
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[fast] > nums[slow]:
            slow += 1  # TODO:一定要注意这里的顺序！
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1

def removeDuplicates(nums):
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[fast] > nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
        else:
            fast += 1
    return slow + 1