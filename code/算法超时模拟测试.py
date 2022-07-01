import time

def func1(n):
    k = 0
    for i in range(n):
        k += 1

def func2(n):
    k = 0
    for i in range(n):
        for j in range(n):
            k += 1

def func3(n):
    k = 0
    for i in range(n):
        j = 1
        while j < n:
            k += 1
            j = j * 2
def main():
    n = input("输入规模：")
    start_time = time.time()
    # func1(int(n))
    func2(int(n))
    # func3(int(n))
    end_time = time.time()
    print(f"耗时：{end_time - start_time}ms")
    
    
if __name__ == '__main__':
    main()