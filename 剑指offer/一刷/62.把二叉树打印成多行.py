# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):

        if root == None:
            return []

        normal = [root]
        res = []

        while normal:
            res.append([node.val for node in normal])

            temp = []
            for node in normal:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            normal = temp
        return res


"""
61。62。22属于同一类型题的变种

这题主要利用了一个递推式，把一层的node都直接append进结果里
这里的加node的过程要与递推式分开，因为外循环每执行一次，都要求append
所以加node只能在一个内循环里解决了，这个跟前面的两题有点不一样

"""

