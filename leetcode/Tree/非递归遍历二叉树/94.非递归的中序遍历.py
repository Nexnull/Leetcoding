# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        left root right
        """
        res = []
        stack = []

        cur = root
        while cur or stack:
            #当还有左节点的时候，一直往深处遍历，一遍遍历一遍往stack里放
            #因为后放进去的先出来
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop(-1)
            res.append(cur.val)
            cur = cur.right

        return res




"""
来源,leetcode答案
time O(n) space O(n)
这题和后序遍历又有点不一样，因为后序遍历是可以完全反过来的，因为走 root, left ,right, 
根节点和子节点是完全分开的，反向操作是比较简单的
那么这题怎么写

1.我们先创建一个stack，cur = root
2.然后我们用这个cur一直向左找，然后每经过一个点，我们就把当前节点放入stack中
这样做是使得，最左边的点，在最上面，最靠近root的点，在最下面
3.遍历到了以后，开始pop（），那么出来的node就是最左边的，加进res,
  同时我们以当前这个点作为root，开始向右边探查

4.重复这种操作，直到所有的都完成

"""

