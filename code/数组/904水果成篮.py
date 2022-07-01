# TODO:leetcode这个题目的题解中有最大滑窗最小滑窗的模板

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        i, j = 0, 0
        res = 0
        classMap = defaultdict(int)  # 当key不存在时返回0
        classCat = 0
        
        # 移动滑窗右边界
        while j < len(fruits):
            # 判断当前是否满足条件
            if classMap[fruits[j]] == 0:  # 如果此时要摘的类别之前没有出现过，则类别数需要加1
                classCat += 1
            classMap[fruits[j]] += 1  # 如果此时的类别之前就已经出现过，则只需要数目加1
            
            # 若不满足条件，移动i
            while classCat > 2:
                if classMap[fruits[i]] == 1:  # 如果类别数已经超过了2，则需要改变起始位置。如果起始位置的类别的数目只有一个，去掉后类别数需要减1。
                    classCat -= 1
                classMap[fruits[i]] -= 1
                i += 1
            
            # 一旦满足条件，更新结果
            res = max(res, j - i + 1)
            j += 1
        return res
