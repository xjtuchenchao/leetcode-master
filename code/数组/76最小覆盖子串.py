from collections import defaultdict

class Solution:
    def minWindow(self, s, t):
        i, j = 0, 0
        needMap = defaultdict(int)
        needCat = len(t)
        res = ''

        for char in t:
            needMap[char] += 1
        
        # 移动滑窗右边界
        while j < len(s):
            # 判断是否满足条件
            if s[j] in needMap:  # 如果needMap中存在key
                if needMap[s[j]] > 0:  # 且数量大于0
                    needCat -= 1
                needMap[s[j]] -= 1
            
            # 一旦满足条件，尽可能地压缩i，并且不断更新结果
            while needCat == 0:
                if not res or j - i + 1 < len(res):  # 取较小的那个
                    res = s[i:j+1]
                
                if s[i] in needMap:  # 如果key存在，则更新起始位置时需要将s[i]对应的加上1
                    if needMap[s[i]] == 0:
                        needCat += 1
                    needMap[s[i]] += 1
                i += 1
            j += 1
        return res