'''
    遇到一颗二叉树的题目时的通用思考过程是：
    1.是否可以通过遍历一遍二叉树得到答案？如果可以，用一个traverse函数配合外部变量来实现。
    2.是否可以定义一个递归思维，通过子问题（子树）的答案推导出原问题的答案？如果可以，
    写出这个递归函数的定义，并充分利用这个函数的返回值。
    3.无论使用哪一种思维模式，你都要明白二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。
'''

# 前序位置是刚刚进入节点的时刻，后续位置是即将离开节点的时刻。
# 但这里面大有玄机，意味着前序位置的代码只能从函数参数中获取父节点传来的数据，而后续位置的代码
# 不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据。

# eg:给你一颗二叉树，问两个简单的问题
# 1.如果把根节点看作第一层，如何打印出每一个节点所在的层数？
# 2.如何打印出每个节点的左右子树各有多少节点？

'''
    这两个问题的根本区别在于：一个节点在第几层，你从根节点遍历过来的过程就能顺带记录，而以一个节点为根节点的
    整颗子树有多少个节点，你需要遍历完子树之后才能数清楚。
    总结：后续位置的特点就是只有后续位置才能通过返回值获取子树的信息。换句话说，
        一旦你发现题目和子树相关，那大概率要给函数设置合理的定义和返回值，在后续位置写代码了！
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1.打印每一个节点的层数
def printLevel(root, level):
    if not root:
        return 0
    print("节点%s在第%d层" % (root, level))
    printLevel(root.left, level+1)
    printLevel(root.right, level+1)
root = TreeNode()
printLevel(root, 1)

# 2.打印出每个节点的左右子树各有多少个节点
def count(root):
    if not root:
        return 0
    left = count(root.left)
    right = count(root.right)
    print("节点%s的左子树有%d个节点，右子树有%d个节点" % (root, left, right))
    return left + right + 1