#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        res = [root.val] + left + right
        return res

    # def __init__(self):
    #     self.res = []
    
    # def preorderTraversal(self, root):
    #     if not root:
    #         return []
    #     self.res.append(root.val)
    #     self.preorderTraversal(root.left)
    #     self.preorderTraversal(root.right)
    #     return self.res

# @lc code=end

