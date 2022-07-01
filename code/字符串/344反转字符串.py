class Solution:
    def reverseString(self, s):  # 这里输入的s是一个list
        left, right = 0, len(s) - 1
        while left < right:  # 之所以不取等号，是因为等于的情况下不需要做任何操作。
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1
        