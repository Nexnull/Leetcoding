
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        if t1 and not t2: return t1
        if not t1 and t2: return t2
        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

"""
https://algocasts.io/episodes/ezpljkmE
// Time: O(n), Space: O(n)
要去n个节点，时间为n，层数可能有n层，则为n
答案：
1.假如有两棵树
两棵树的相同节点有值的话，那么他们的值相加
两棵树的相同节点无值的话，那么那个位置为空
两棵树的相同节点一个有节点，一个没节点的话，那么那个位置换上有节点的那个值

              
"""