"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [-1,2,3]

       -1
      / \
     2   3

Output: 2 + -1 + 3 = 4 ,包括树的任意节点哦
"""

import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = -sys.maxsize
        self.helper(root)
        return self.res

    def helper(self, root):
        if root == None: return 0
        leftmax = max(self.helper(root.left), 0)
        rightmax = max(self.helper(root.right), 0)
        self.res = max(self.res, root.val + leftmax + rightmax)
        return root.val + max(leftmax, rightmax)


"""
https://algocasts.io/episodes/deG4BbW1
为什么我们要把max的收集放进helper()
1.假如我们在主函数对才对left ,root, right 的value进行max处理和判断，那么在主函数里计算总max需要遍历n次
  然后helper()里面，又要对树进行一遍遍历，所以时间复杂度是 On^2
2.但是假如说我们在辅助函数里对max进行处理，那么主函数只用调用一次，因为辅助函数里其实也会遍历所有的节点，
  只要我们记录好max值，那我们一样可以得到答案，所以这个是On^2

答案：
1.这题的路径和，意味着只要是节点相连的，都可以算一条路径，所以和之前的从上往下的是不一样的
2.这题有负数，所以我们在找子树的最大和时，一定要让max(子树和，0），避免负数入选
3.在每一轮的左右子树最大值求出来后，我们都要更新max[0]的值
4.为什么传的是max[0],因为函数传列表传的是地址，传数字传的不是同一个地址，要保证这个max是一样的



"""