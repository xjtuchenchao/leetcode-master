'''
    递归时间复杂度本质上:递归的次数 * 每次递归的时间复杂度
'''
import time

def fibonacci(n):
    '''时间复杂度为:O(2^n)'''
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)    # TODO:耗时的罪魁祸首就是这里的两次递归

def fibonacci2(first, second, n):  # 这里就相当于用first和second来记录当前相加的两个数值，此时就不用两次递归了。
    '''时间复杂度为:O(n)'''         # 不过需要注意的是first和second的初始值
    if n <= 0:
        return 0
    if n < 3:
        return 1
    elif n == 3:
        return first + second
    else:
        return fibonacci2(second, first+second, n-1)

def binary_search(list, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if list[mid] == x:
            return mid
        if list[mid] > x:
            return binary_search(list, l, mid-1, x)
        return binary_search(list, mid+1, r, x)
    return -1
        

def main():
    n = input("输入规模：")
    start_time = time.time()
    print(fibonacci2(1, 1, int(n)))
    end_time = time.time()
    print(f"耗时：{end_time - start_time}ms")

if __name__ == '__main__':
    main()