"""
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
"""
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        self.helper(root, 0)
        return root


    def helper(self, root, val):
        if not root:
            return val

        # 注意这里的递归是咋写的
        cur = self.helper(root.right, val)
        root.val += cur
        return self.helper(root.left, root.val)

"""
Time: O(n), Space: O(n)
https://algocasts.io/episodes/8eGxrAWM
根据题目给的树， 按照中序遍历的走法是， 2 5 13
然后这题要求的是， 先节点的值，等于本节点的值 加上所有后节点的值之和
所以结果是 20（2+5+13） 18（5+13） 13(13+0)
由于我们处于节省时间空间的考虑。 所以我们从最后一个节点开始遍历，那就是中序遍历的反向 rigth root left
"""