class Solution:
    def reverseStr(self, s, k):
        def reverse(strs):
            left, right = 0, len(strs) - 1
            while left < right:
                strs[left], strs[right] = strs[right], strs[left]
                left += 1
                right -= 1
            return strs
        
        # length = len(s)
        # res = list(s)
        # for i in range(0, length, 2*k):
        #     if k <= length - i <= 2*k:
        #         res[i:i+k] = reverse(res[i:i+k])
        #     elif length - i < k:
        #         res[i:length] = reverse(res[i:length])
        #     else:
        #         res[i:i+k] = reverse(res[i:i+k])
        # return ''.join(res)
        
        res = list(s)
        for cur in range(0, len(s), 2*k):
            res[cur:cur+k] = reverse(res[cur:cur+k])  # NOTE:如果索引超出了最大长度，则只会返回到最后一个字符，这样可以避免一些不必要的边界条件判断
        return ''.join(res)
    
    def reverseStr2(self, s, k):
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p:p2][::-1] + s[p2:]
            p = p + 2 * k
        return s
        
            