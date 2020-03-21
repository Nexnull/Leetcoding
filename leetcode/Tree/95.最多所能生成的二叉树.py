"""
这题要求你把所有可能的二叉树都生成出来
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []

        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]

        cur_tree = []

        for i in range(start, end + 1):
            l_subtree = self.helper(start, i - 1)
            r_subtree = self.helper(i + 1, end)

            for l in l_subtree:
                for r in r_subtree:
                    # 我们在这里创造一个新的节点
                    cur = TreeNode(i)
                    cur.left = l
                    cur.right = r
                    cur_tree.append(cur)
        return cur_tree

"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode/
这题我们使用递归的方法来做， 我们假设在 start ~ end 中，我们定下一个节点
那么节点的子树的都要比它小，节点右边的子树都要比他大
假如说 start > end, 返回[]
假如说 start == end, 返回[start], 这是我们递归的最底层
然后我们就这样获得一个所有左子树的列表和一个所有右子树的列表
每次从子树中抽出一个元素，和当前node拼起来，就形成一个满足条件的二叉搜索树
然后把所有的结果都放在一起就完了
"""