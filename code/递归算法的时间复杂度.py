'''求x的n次方'''

def func1(x, n):
    '''直接使用循环解决:时间复杂度为O(n)'''
    result = 1
    for i in range(n):
        result *= x
    return result

def func2(x, n):
    '''使用递归解决:时间复杂度为O(n)'''
    if n == 0:
        return 1
    return func2(x, n-1) *  x

def func3(x, n):
    '''使用递归解决:时间复杂度为0(n)'''  # TODO:特别注意这个算法的时间复杂度分析
    if n == 0:
        return 1
    if n % 2 == 1:
        return func3(x, n // 2) * func3(x, n // 2) * x
    return func3(x, n // 2) * func3(x, n // 2)

def func4(x, n):
    '''使用递归解决:时间复杂度为O(logn)'''
    if n == 0:
        return 1
    t = func4(x, n // 2)
    if n % 2 == 1:
        return t * t * x
    return t * t

def main(x, n):
    print(func1(x, n), func2(x, n), func3(x, n), func4(x, n))

if __name__ == '__main__':
    main(2, 4)
    