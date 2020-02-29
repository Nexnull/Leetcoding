class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归写法：（深度优先）
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径

    def FindPath(self, root, expectNumber):
        res = []

        if root == None:
            return res
        self.sums = expectNumber
        self.helper(root, res, [root.val])

        return res


    def helper(self, root, res ,path):

            if root.left == None and root.right == None and sum(path) == self.sums:
                res.append(path)
            if root.left != None:
                self.helper(root.left,res,path + [root.left.val])
            if root.right != None:
                self.helper(root.right,res,path + [root.right.val])


#非递归写法：
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # 当为树的最后一个节点且满足条件时
        if root == None:
            return []

        res = []
        stack = []
        stack.append((root,[root.val]))
        while stack:
            node , path = stack.pop(0)
            if node.left == None and node.right == None and sum(path) == expectNumber:
                res.append(path)
            if node.left != None:
                stack.append((node.left, path + [node.left.val]))
            if node.right != None:
                stack.append(( node.right , path + [node.right.val]))

        #帮助res里的list长度是按照从大到小的顺序排列的
        res.sort(key=lambda x: len(x), reverse=True)
        return res





"""
这题等于leetcode 的path sum 2
我的想法是:边界条件写好了，没语法错误，但是就是跑的是空列表，
思路是 期望值 - node的值，然后当为0的时候，就把它加进res中

问题：每一个path 要怎么保持独立，最后加到res里:
每一次递归所产生的path都是独立，我们要做的就是，当path完成以后，把正确的path给加进res里

"""
