#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
#     def __init__(self):
#         self.maxDiameter = 0
    
#     def maxDepth(self, root):
#         '''求节点的最大深度'''
#         if not root:
#             return 0
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
#         return 1 + max(left, right)

#     def traverse(self, root):
#         '''求最大直径'''
#         if not root:
#             return 
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
#         myDiameter = left + right
#         self.maxDiameter = max(self.maxDiameter, myDiameter)
#         self.traverse(root.left)
#         self.traverse(root.right)
        
#     def diameterOfBinaryTree(self, root):
#         self.traverse(root)
#         return self.maxDiameter

class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def maxDepth(self, root):
        '''求节点的最大深度'''
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        myDiameter = left + right
        self.maxDiameter = max(self.maxDiameter, myDiameter)
        return 1 + max(left, right)
        
    def diameterOfBinaryTree(self, root):
        self.maxDepth(root)
        return self.maxDiameter
# @lc code=end

