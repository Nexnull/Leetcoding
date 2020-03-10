"""
Given a binary tree, find its minimum depth.
"""

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # 假如说一边是none, 一遍非none,我们要走的是有node的一边，所以取max
        elif not root.left or not root.right:
            return 1 + max(self.minDepth(root.left),self.minDepth(root.right))
        # 假如说两边都有node, 或者两边都没node
        # 那么都是取 1 + min
        else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))

"""
答案：
和求最大的深度一样，可以用递归来写，但是这题会多一些限制
例如同样用简单粗暴的方法return 1 + min(self.minDepth(root.left),self.minDepth(root.right))  
        1
          2
遇到这种情况，就只会返回1了，因为它会优先选少节点的一边



所以我们需要保证，遍历要遍历在有节点的那一边，且高度最低
所以我们加了第二个判断。
1.假如说遍历到空节点了，返回0，说明这层没高度了

2.当一边有node,一边没node时，我们需要返回的是有node的那一边的，因为我们要找现实存在的最低高度（最重要）
**我们一定要写成not root.left or not root.right 这种形式，因为root.left != None这样判断的话，并不能说明右边
有没有node,这样会漏判
**而且not root.left or not root.right包含了两边都没的情况，这时候应该返回1，这也是root.left!= None所覆盖不到的

3.假如说都找完了，返回最低的 + root本身的高度

或者也可以第2步也可以这样写
if not root.left:
    return 1 + self.minDepth(root.right)
if not root.right:
    return 1 + self.minDepth(root.left)
    
注意：


"""
