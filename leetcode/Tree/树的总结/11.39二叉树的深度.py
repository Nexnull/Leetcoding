"""
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, root):
        if not root:
            return 0

        res = 0
        queue = [root]

        while queue:
            temp = [node for node in queue]
            res += 1
            level = []

            for node in temp:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
        return res


#递归写法
class Solution:
    def TreeDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.TreeDepth(root.left) , self.TreeDepth(root.right))




"""
求深度，第一反应就是bfs,因为bfs是逐层遍历的
用来求深度的话很方便
我的想法是：
首先给个res = []，用来存放每个root到每个末节点的长度
然后再做个bfs遍历
后面发现不用这么复杂，其实这题和把二叉树打印成多行是同一道题
我们只需要用一个sum变量来记录总共遍历了多少层，返回就行了

remark:这种树的层状和一般的bfs还是有一点点不同，需要记忆

"""