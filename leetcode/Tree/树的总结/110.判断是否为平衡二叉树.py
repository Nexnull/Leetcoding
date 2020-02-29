"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

平衡二叉树（Balanced Binary Tree）它是一棵空树或它的左右两个子树的高度差的绝对值不超过1,
意味着其中一边可以是缺一个node的。这题的做法是要计算每个node的高度差
再换而言之，就是求每一个node的深度
第一种做法，从上开始往下（先判断主树，再判断子树）。看高度是否满足子树的需求
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, root):
        if not root:
            return True

        return abs(self.helper(root.left) - self.helper(root.right))<= 1 and \
               self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)

    def helper(self,root):
        if not root:
            return 0

        return 1 + max(self.helper(root.left), self.helper(root.right))


"""
上面的递归做法效率是比较低的，因为有很多点是经过多次重复遍历过的
还有一个小陷阱，主函数的return 里的递归应该还是主函数，且主函数递归的终止条件应该是返回的是True.
因为出现{} {1}这种情况的话，都是应该返回true的
"""

"""
如果改为从下往上遍历（先判断子树，再判断主树），如果子树是平衡二叉树，则返回子树的高度；
如果发现子树不是平衡二叉树，则直接停止遍历，这样至多只对每个结点访问一次。
"""
class Solution:
    def IsBalanced_Solution(self, root):
        if not root:
            return True

        return self.helper(root) != -1

    def helper(self,root):
        if root == None:
            return 0

        #看左子树的子树是不是平衡二叉树
        left = self.helper(root.left)
        if left == -1:
            return -1

        #看右子树的子树是不是平衡二叉树
        right = self.helper(root.right)
        if right == -1:
            return -1

        #判断左右子树的高度差满足要求了吗
        #这里要大于1，因为只有大于1才可以满足不平衡
        if abs(left - right) > 1:
            return -1

        #说明左右子树本身是平衡二叉树，返回root+子树的最大高度
        return 1 + max(left,right)