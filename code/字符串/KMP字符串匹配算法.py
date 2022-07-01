'''
    前缀：指字符串中不包含最后一个字符的所有以第一个字符开头的连续字串。
    后缀：指不包含第一个字符的所有以最后一个字符结尾的连续子串。
    前缀表的作用：当字符在某个位置匹配失败后，不是从模式串的起始处开始重新匹配，而是跳到某个位置处开始匹配，
    这样就可以减少匹配的次数。具体来说，就是将模式串前缀与字符串的后缀进行对齐，再重新匹配。
'''
# 如何计算前缀表？

next_array = []
def getNext(p):
    next_array.append(0)
    x = 1
    now = 0
    while x < len(p):
        if p[now] == p[x]:  # 如果p[now] == p[x],则可以向右扩展一位
            now += 1
            x += 1
            next_array.append(now)
        elif now:  # 如果不等，缩小now，改成next_array[now-1]
            now = next_array[now-1]
        else:  # now已经为0了，无法再缩小，故next_array[x] = 0
            next_array.append(0)
            x += 1

def search(s, p):  # s为主字符串，p为模式串
    tar = 0  # 主串中将要匹配的位置
    pos = 0  # 模式串中将要匹配的位置
    while tar < len(s):
        if s[tar] == p[pos]:  # 若两个字符相等，则tar、pos都向右移动一位
            tar += 1
            pos += 1
        elif pos:  # 如果不相等（即匹配失败了），且pos！=0，则依据next_array移动标尺
            pos = next_array[pos-1]
        else:  # 在模式串的第一个字符处匹配失败，直接在主串上右移一位
            tar += 1
        if pos == len(p):  # pos走到了len(p),匹配成功
            print(tar - pos + 1)
            pos = next_array[pos-1]  # 将pos归位


            