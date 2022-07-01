'''
    概念解释：所谓二叉树的【直径】长度，就是任意两个节点之间的路径长度。
             两节点之间的路径长度是以他们之间边的数目表示。
             且这条路径可能穿过也可能不穿过根节点。
             
    总结：遇到子树问题，首先想到的是给函数设置返回值，然后在后续位置做文章。
    
'''
# 解决题目的关键在于：每一条二叉树的【直径】长度，就是一个节点的左右子树的最大深度之和。
# 因此直截了当的思路就是遍历整棵树的每个节点，然后通过每个节点的左右子树的最大深度算出每个节点的【直径】，
# 最后把所有【直径】求个最大值即可。

# 前序位置处理：由于前序位置无法获取子树信息，所以只能让每个节点调用maxDepth函数去算子树的深度。
class Solution:
    def __init__(self):
        self.maxDiameter = 0
    
    def maxDepth(self, root):
        '''求节点的最大深度'''
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

    def traverse(self, root):
        '''求最大直径'''
        if not root:
            return 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        myDiameter = left + right
        self.maxDiameter = max(self.maxDiameter, myDiameter)
        self.traverse(root.left)
        self.traverse(root.right)
        
    def diameterOfBinaryTree(self, root):
        self.traverse(root)
        return self.maxDiameter

# 优化：把计算【直径】的逻辑放到后续位置，准确来说是放在maxDepth的后续位置的，因为maxDepth的后续位置是知道左右子树的最大深度的。
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