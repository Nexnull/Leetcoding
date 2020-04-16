"""
这个题目说的是，给你一棵二叉树，你要计算出这棵树的直径。
二叉树的直径定义为树上任意两个节点之间最长路径的长度。
其中，两个节点之间的路径不一定要经过根节点。
"""

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.findDepth(root)
        return self.res

    def findDepth(self, root):
        if not root:
            return 0

        left = self.findDepth(root.left)
        right = self.findDepth(root.right)

        # 这一步记录了，经过当前root的最大长度，所以是left + right
        self.res = max(self.res, left + right)

        # 返回却要返回，从当前root到leaf的最长距离，供left,right使用
        return max(left, right) + 1

"""
https://algocasts.io/episodes/nwp8ArW7
答案：
Time Complexity: O(N). We visit every node once.
Space Complexity: O(N), the size of our implicit call stack during our depth-first search.
0。因为当前节点的最大直径，等于它的左右节点的最大深度和（不加上自己），所以我们left + right就可以了

   ！！我们做题的时候，要搞清楚，到底要不要把当前节点的高度给算进去，这决定了left+right还要不要+1
 
1。假如说，我们要求经过根节点的最长路径，那么我们求出 max(left) + max(right) + 1就可以了
    但是这题，我们没有限定一定要经过根节点，所以最大长度可以由任意节点产生，因此我们要在每一次调用中，
    用self.res = max(self.res, left + right)，来更新最大长度


"""