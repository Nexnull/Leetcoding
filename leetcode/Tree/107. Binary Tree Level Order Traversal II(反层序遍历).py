"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root is None: return []

        res = []
        queue = [root]

        while queue:
            res.append([node.val for node in queue])
            level = []

            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            queue = level

        return res[::-1]

"""
其实就是树的层级遍历，因为我们要把每一层都作为一个List储存在res里，最后反转一遍

所以我们在bfs的时候，把每一层的结果都放到一个 [x] 里，最后让这个queue = [x]
然后在开头都时候把queue里的每个元素都放进res里
"""