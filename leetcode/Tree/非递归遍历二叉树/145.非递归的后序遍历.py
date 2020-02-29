"""
给定你一棵二叉树，让你用非递归的方式完成后序遍历
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        left right root
        """
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop(-1)
            res.insert(0, node.val)
            # left right root
            # so , we should push right later, so that we can pop right first

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        return res

"""
非递归的树遍历，要数后序遍历最难

做法：
正常的后续遍历都是 left right root，最后才访问root
但是在非递归的情况下，这样的先走子节点，再走根节点，是有点反人类的，所以我们要如何巧妙的处理这种情况呢？

我们可以按照 root,right,left的方法去访问，但是添加顺序是反向添加的
那么不就等于是left,right,root了吗？

  3
1  2
例如 l r root,[1,2,3]， 
那我们反向访问，root,r,l,不就是[3,2,1],我们插入顺序变成从前插入的话，不就等于了
[3],[2,3],[1,2,3]了吗

最后直接输出结果就好
"""