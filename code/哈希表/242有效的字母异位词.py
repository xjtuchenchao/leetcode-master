class Solution:
    def isAnagram(self, s, t):
        # record = [0] * 26
        # for i in range(len(s)):
        #     record[ord(s[i]) - ord("a")] += 1  # ord()返回对应的 ASCII 数值
        # for i in range(len(t)):
        #     record[ord(t[i]) - ord("a")] -= 1
        # for i in range(26):
        #     if record[i] != 0:
        #         return False
        # return True
        
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for x in s:
            s_dict[x] += 1
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict