
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k == 0:
            return None
        res = []

        def midOrder(root):
            if not root:
                return None
            else:
                midOrder(root.left)
                res.append(root)
                midOrder(root.right)
            return res

        midOrder(pRoot)
        if k > len(res):
            return None
        else:
            return res[k-1]





"""
这题的思维可能需要一点反转
正常的二叉搜索树应该是 小 root 大，但是第几小真的不好找
因为正常的都是，比root小多少个
所以这个题到底怎么写？


答案：
根据剑指offer的说法，BST中序遍历过后产生的数组是从小到大顺序的
然后可以根据这个数组来找到答案

稍微根据63题的代码修改下就出结果了
"""