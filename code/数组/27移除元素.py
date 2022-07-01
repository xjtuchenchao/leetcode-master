'''
    27.移除元素
'''
# 方法一：暴力解法
def violent_search(nums, val):
    length = len(nums)
    for i in range(length):
        if nums[i] == val:
            j = i + 1
            while j < length:
                nums[j-1] = nums[j]
            i -= 1
            length -= 1
    return length

# 方法二：双指针法（快指针去寻找新数组的元素，慢指针指向新数组下标的位置）相对顺序保持一致
def removeElement(nums, val):
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] == val:  # 如果相等，fast指针就要往后移动一位
            fast += 1
        else:
            nums[slow] = nums[fast]  # 如果不相等，快慢指针都要往后移动一位
            fast += 1
            slow += 1
    return slow

# 方法三：相向双指针法(左指针指向等于val的位置，右指针指向不等于val的位置) 相对顺序不再一致
def removeElement2(nums, val):
    left, right = 0, len(nums) - 1
    while left <= right:
        while left <= right and nums[left] != val:  # NOTE:注意这里为什么还要判断left是否小于等于right，是因为这里会改变left的值，而如果不满足left小于等于right了，就不需要运行循环语句了。
            left += 1
        while left <= right and nums[right] == val:
            right -= 1
        if left < right:
            nums[left] = nums[right]  # NOTE:除了赋值外，还需要改变指针的位置，别忘记了！
            left += 1
            right -= 1
    return left
            