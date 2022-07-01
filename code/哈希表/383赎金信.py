class Solution:
    def canConstruct(self, ransomNote, magazine):
        # record = [0] * 26
        # for i in range(len(ransomNote)):
        #     record[ord(ransomNote[i]) - ord("a")] += 1  # ord()返回对应的 ASCII 数值
        # for i in range(len(magazine)):
        #     record[ord(magazine[i]) - ord("a")] -= 1
        # for i in range(26):
        #     if record[i] > 0:  # 如果还有大于0的，就不能
        #         return False
        # return True
        
        # from collections import defaultdict
        # hashmap = defaultdict(int)
        # for x in magazine:
        #     hashmap[x] += 1
        # for x in ransomNote:
        #     value = hashmap.get(x)
        #     if value is None or value == 0:
        #         return False
        #     else:
        #         hashmap[x] -= 1
        # return True
        
        hashmap = dict()
        for s in ransomNote:
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1
        for l in magazine:
            if l in hashmap:
                hashmap[l] -= 1
        for key in hashmap:
            if hashmap[key] > 0:
                return False
        return True