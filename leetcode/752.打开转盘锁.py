#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    # 1.单向BFS
    # def openLock(self, deadends: List[str], target: str) -> int:
    #     def plusOne(s, j):
    #         if int(s[j]) == 9:
    #             ch = s[:j] + '0' + s[j+1:]
    #         else:
    #             ch = s[:j] + f'{int(s[j])+1}' + s[j+1:] if j < len(s) - 1 else s[:j] + f'{int(s[j])+1}'
    #         return ch
        
    #     def minusOne(s, j):
    #         if int(s[j]) == 0:
    #             ch = s[:j] + '9' + s[j+1:]
    #         else:
    #             ch = s[:j] + f'{int(s[j])-1}' + s[j+1:] if j < len(s) - 1 else s[:j] + f'{int(s[j])-1}'
    #         return ch
        
    #     # 记录所有跳过的死亡密码
    #     deads = set()
    #     for str in deadends:
    #         deads.add(str)
    #     # 记录已经穷举过的密码，防止走回头路
    #     visited = set()
    #     queue = ["0000"]
    #     step = 0
    #     visited.add("0000")

    #     while queue:
    #         sz = len(queue)
    #         for i in range(sz):
    #             cur = queue.pop(0)
    #             if cur in deads:
    #                 continue
    #             if cur == target:
    #                 return step
                
    #             for j in range(4):
    #                 up = plusOne(cur, j)
    #                 if up not in visited:
    #                     queue.append(up)
    #                     visited.add(up)
    #                 down = minusOne(cur, j)
    #                 if down not in visited:
    #                     queue.append(down)
    #                     visited.add(down)
    #         step += 1
    #     return -1
    
    # 2.双向BFS
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusOne(s, j):
            if int(s[j]) == 9:
                ch = s[:j] + '0' + s[j+1:]
            else:
                ch = s[:j] + f'{int(s[j])+1}' + s[j+1:] if j < len(s) - 1 else s[:j] + f'{int(s[j])+1}'
            return ch
        
        def minusOne(s, j):
            if int(s[j]) == 0:
                ch = s[:j] + '9' + s[j+1:]
            else:
                ch = s[:j] + f'{int(s[j])-1}' + s[j+1:] if j < len(s) - 1 else s[:j] + f'{int(s[j])-1}'
            return ch
        
        # 记录所有跳过的死亡密码
        deads = set()
        for str in deadends:
            deads.add(str)
        # 记录已经穷举过的密码，防止走回头路
        visited = set()
        q1 = set()
        q2 = set()
        
        step = 0
        q1.add('0000')
        q2.add(target)

        while q1 and q2:
            if len(q1) > len(q2):
                temp = q1
                q1 = q2
                q2 = temp
            
            # 哈希集合在遍历的过程中不能修改，用temp存储扩散结果
            temp = set()
            
            # 将q1中的所有节点向四周扩散
            for cur in q1:
                if cur in deads:
                    continue
                if cur in q2:
                    return step
            
                visited.add(cur)
                
                # 将一个节点的未遍历相邻节点加入到集合中
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        temp.add(up)
                        
                    down = minusOne(cur, j)
                    if down not in visited:
                        temp.add(down)
                    
            step += 1
            q1 = q2
            q2 = temp
        return -1
                
        
# @lc code=end

