# 1.遍历二叉树的思路
# 我们熟悉的解法就是用遍历的思路
class Solution:
    def __init__(self):
        self.res = []
    
    def preorderTraversal(self, root):
        if not root:
            return []
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res

# 2.分解问题的思路
# 我们知道前序遍历的特点是根节点的值排在首位，接着是左子树的前序遍历结果，最后是右子树的遍历结果。
# 这样的话我们就将问题进行了分解：即一颗二叉树的前序遍历结果 = 根节点的值 + 左子树的前序遍历结果 + 右子树的前序遍历结果
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        res = [root.val] + left + right
        return res