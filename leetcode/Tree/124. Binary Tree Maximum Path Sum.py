"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。
该路径至少包含一个节点，且不一定经过根节点。
Example 1:
Input: [-1,2,3]

       -1
      / \
     2   3

Output: 2 + -1 + 3 = 4 ,包括树的任意节点哦!!
"""

import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        #因为有可能出现 【-3】 这种case
        self.res = -sys.maxsize
        self.helper(root)
        return self.res

    def helper(self, root):
        if root == None: return 0

        #这题有负数，所以我们在找子树的最大和时，一定要让max(子树和，0），避免负数入选
        left_max = max(self.helper(root.left), 0)
        right_max = max(self.helper(root.right), 0)

        # 把经过当前节点的所有path都找出来，然后求出他们的最大值
        curnode_sum = root.val + left_max + right_max

        #self.res代表的是经过上一个节点的所有路径的最大值
        #curnode_sum代表的是经过当前节点的所有路径的最大值
        self.res = max(self.res, curnode_sum)

        #为了给left_max传值的return, 为了保证是一条路径，所以我们左右节点只能取一个
        return root.val + max(left_max, right_max)


"""
https://algocasts.io/episodes/deG4BbW1
1.假如我们在主函数对才对left ,root, right 的value进行max处理和判断，那么在主函数里计算总max需要遍历n次
  然后helper()里面，又要对树进行一遍遍历，所以时间复杂度是 On^2
2.但是假如说我们在辅助函数里对max进行处理，那么主函数只用调用一次，因为辅助函数里其实也会遍历所有的节点，
  只要我们记录好max值，那我们一样可以得到答案，所以这个是On^2

答案：
这题其实就是 找出最大子序列（51）的和的二叉树版本
根据那题的思想，我们要保持一个子序列和，当子序列和<0的时候，我们就要重新开始计算子序列和
因为 一个负数无论 + 什么序列， 都不如一个序列重新相加大


相似体形：
51
687
534ß
"""