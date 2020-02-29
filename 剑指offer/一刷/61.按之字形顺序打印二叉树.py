# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, root):
        def averageOfLevels(self, root):
            l = []
            if not root:
                return []
            normal = [root]
            reverse = []
            flag = 1

            while len(normal) or len(reverse):
                if flag == 1:
                    t = normal.pop(0)
                else:
                    t = reverse.pop(0)

                l.append(t.val)

                # 下一层从右往左打
                if flag == 1:
                    if t.right:
                        reverse.append(t.right)
                    if t.left:
                        reverse.append(t.left)

                # 下一层从左往右打
                elif flag == 2:
                    if t.left:
                        normal.append(t.left)
                    if t.right:
                        normal.append(t.right)

                if len(normal) == 0:
                    flag = 2
                if len(reverse) == 0:
                    flag = 1

            return l

"""
跟逐层打印很像，只不过逐层打印只需要一个容齐来陈放node,
这里需要两个，一个储存正序，一个储存倒叙
牛客网没通过，但是leetcode上显示可以
"""