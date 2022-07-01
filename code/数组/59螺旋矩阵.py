# 循环不变量原则  左闭右开原则或者左开右闭原则

# 一律坚持左闭右开的原则进行模拟
class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n // 2, n // 2
        count = 1
        
        for offset in range(1, loop+1):
            for i in range(starty, n-offset):  # 从左到右，左闭右开
                matrix[startx][i] = count
                count += 1
            for i in range(startx, n-offset):  # 从上到下，左闭右开
                matrix[i][n-offset] = count
                count += 1
            for i in range(n-offset, starty, -1):  # 从右到左
                matrix[n-offset][i] = count
                count += 1
            for i in range(n-offset, startx, -1):  # 从下到上
                matrix[i][starty] = count
                count += 1
            startx += 1  # 更新起始点
            starty += 1
        if n % 2 != 0:
            matrix[mid][mid] = count
        return matrix


class Solution:
    def generateMatrix(self, n):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n**2):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy
        return matrix

class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        num = 1
        left, right, top, bottom = 0, n-1, 0, n-1
        
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            for row in range(top+1, bottom+1):
                matrix[row][right] = num
                num += 1
            if left < right and top < bottom:
                for col in range(right-1, left, -1):
                    matrix[bottom][col] = num
                    num += 1
                for row in range(bottom, top, -1):
                    matrix[row][left] = num
                    num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix
        

