class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        top, left, bottom, right = 0, 0, m-1, n-1
        result = []
        
        while left <= right and top <= bottom:  # TODO:判断条件该怎么确定？画图
            for col in range(left, right+1):
                result.append(matrix[top][col])
            for row in range(top+1, bottom+1):
                result.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right-1, left-1, -1):
                    result.append(matrix[bottom][col])
                for row in range(bottom-1, top, -1):
                    result.append(matrix[row][left])
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return result