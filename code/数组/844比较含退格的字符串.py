# TODO:可以再看一遍

def backspaceCompare(s, t):
    p1 = len(s) - 1
    p2 = len(t) - 1
    skipS = 0
    skipT = 0
    while p1 >= 0 or p2 >= 0:
        # 找到不需要跳过的字符
        while p1 >= 0:
            if s[p1] == "#":
                skipS += 1
                p1 -= 1
            elif skipS > 0:
                skipS -= 1
                p1 -= 1
            # elif skipS > 0:  # NOTE:不能一下子全跳过去，因为有可能跳过的字符中有#
            #     p1 -= skipS
            #     skipS = 0
            else:
                break
        # 找到不需要跳过的字符
        while p2 >= 0:
            if t[p2] == "#":
                skipT += 1
                p2 -= 1
            elif skipT > 0:
                skipT -= 1
                p2 -= 1
            # elif skipT > 0:
            #     p2 -= skipT
            #     skipT = 0
            else:
                break
        # 如果指针都大于0
        if p1 >= 0 and p2 >= 0:
            if s[p1] != t[p2]:
                return False
            else:
                p1 -= 1
                p2 -= 1
        # 如果只有一个指针大于0
        elif p1 >= 0 or p2 >= 0:
            return False
        # p1 -= 1
        # p2 -= 1
        # 如果都小于0，其实就可以返回True了
    return True