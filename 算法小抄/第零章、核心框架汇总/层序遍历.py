'''
    二叉树的题型主要是用来培养递归思维的，而层序遍历属于迭代遍历，比较简单。
'''
def levelTraverse(root):
    if not root:
        return []
    queue = [root]
    while queue:
        sz = len(queue)
        for i in range(sz):
            cur = queue.pop(0)
            if not cur.left:
                queue.append(cur.left)
            if not cur.right:
                queue.append(cur.right)

# 如果你对二叉树足够熟悉，可以想到很多方式通过递归函数得到层序遍历结果
res = []

def levelTraverse(root):
    if not root:
        return res
    traverse(root, 0)
    return res

def traverse(root, depth):
    if not root:
        return 
    if len(res) <= depth:  # TODO:为什么是这样的判断条件？不应该取等号就可以解决了吗？
        res.append([])
    res[depth].append(root.val)
    traverse(root.left, depth+1)
    traverse(root.right, depth+1)

res = []
def levelTraverse(root):
    if not root:
        return 
    nodes = []
    nodes.append(root)
    traverse(nodes)
    return res

def traverse(curLevelNodes):
    if not curLevelNodes:
        return 
    nodeValues = []
    nextLevelNodes = []
    for node in curLevelNodes:
        nodeValues.append(node.val)
        if not node.left:
            nextLevelNodes.append(node.left)
        if not node.right:
            nextLevelNodes.append(node.right)
    res.append(nodeValues)  # 前序位置添加结果，可以得到自顶向下的结果
    traverse(nextLevelNodes)
    # res.append(nodeValues)  # 后序位置添加结果，可以得到自底向上的结果