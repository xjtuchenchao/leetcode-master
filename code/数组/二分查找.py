'''
    在一个升序的数组中查找一个值.
    
    写二分法，区间的定义一般为两种，左闭右闭[left, right]，或者左闭右开[left, right)。
    
    1.对于第一种写法，我们定义了target是在一个左闭右闭的区间。那么while循环的时候就需要用left <= right，
    因为left == right是有意义的，所以要使用<=。与此同时，判断条件后，right要赋值为mid-1，因为nums[mid]
    一定不是target，那么接下来要查找的左区间结束下标位置就是mid-1。
    
    2.对于第二种写法，while循环需要使用left < right，因为left == right是没有意义的。
    if nums[mid] > target中需要将right更新为mid，因为当前nums[mid]不等于target，去左区间继续寻找，
    而寻找空间是左闭右开区间，所有right更新为mid，即：下一个查询区间不会去比较nums[mid]。
    
    # NOTE:遵循循环不变量原则。区间的定义就是不变量，在循环中坚持根据查找区间的定义来做边界处理。
'''
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

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
    return -1

def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 3
    print(binary_search2(nums, target))
    
if __name__ == '__main__':
    main()