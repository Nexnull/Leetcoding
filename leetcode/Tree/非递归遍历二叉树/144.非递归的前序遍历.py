# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        root left right
        """
        if not root:
            return []

        res = []
        stack = [root]

        while len(stack) != 0:
            node = stack.pop(-1)
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res


"""
time O(n) space O(n)
答案：
1. 这题简直和145的思路如出一折
2. 只要我们的加入stack的顺序是 right left
   最后pop出来的顺序就是 left right
3. 我们只需要老老实实把当前的node给求出来就好了
"""