'''
    概念解释：所谓最大深度就是指根节点到【最远】叶子节点的最长路径上的节点数。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1.遍历二叉树计算答案的思路
# 最直接的思路：遍历一遍二叉树，用一个外部变量记录每个节点所在的深度，取最大值就可以得到最大深度。
class Solution:
    def __init__(self):
        self.res = 0
        self.depth = 0
    
    def maxDepth(self, root):
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
        self.depth += 1  # NOTE:容易忽视的是，在前序位置增加depth，在后续位置减小depth。离开一个节点返回到上一个节点的时候，depth是需要减1的！
        if not root.left and not root.right:
            self.res = max(self.depth, self.res)
        self.traverse(root.left)
        self.traverse(root.right)
        self.depth -= 1

# 2.分解问题计算答案的思路
# 一颗二叉树的最大深度可以通过子树的最大深度推导出来。
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        res = max(leftMax, rightMax) + 1  # NOTE:整棵树的最大深度等于左右子树的最大深度取最大值，然后再加上根节点自己。
        return res
    