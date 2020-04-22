"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
假如说有多个众数，则要把他们都求出来
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.count = 1
        self.max = 0
        self.pre = None
        self.res = []
        self.helper(root)

        return self.res

    def helper(self, node):
        if not node:
            return

        self.helper(node.left)

        if self.pre != None:
            if self.pre == node.val:
                self.count += 1
            else:
                self.count = 1

        # 当出现一个元素它的出现次数大于前一个众数
        if self.count > self.max:
            self.max = self.count

            #注意有新的众数进来的时候，要把上一个众数给清除掉
            self.res = []
            self.res.append(node.val)

        # 两个出现次数一样的元素都要加进res里去
        elif self.count == self.max:
            self.res.append(node.val)

        self.pre = node.val

        self.helper(node.right)

"""
https://www.youtube.com/watch?v=1FJDyBSfEbo
本题目主体上是用 中序遍历 + 有序数组求众数的做法
本题聪明的解法是，利用一个count 和 max, 以及一个遇到更大数量的数会清空的self.res来解决
                他们是如何相互配合的
"""