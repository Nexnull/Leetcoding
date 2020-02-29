"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        #当为树的最后一个节点且满足条件时

        self.res = []
        if root == None:
            return self.res
        self.sum = expectNumber
        self.helper(root , [root.val])
        return self.res

    def helper(self, root, path):
        if root.left == None and root.right == None and sum(path) == self.sum:
            self.res.append(path)
        if root.left:
            self.helper(root.left , path + [root.left.val])
        if root.right:
            self.helper(root.right , path + [root.right.val])






"""
https://algocasts.io/episodes/k8GNO5pe
回顾这道题，我记得是得以下这种操作：
    def helper(self, root, expectNumber):
        if expectNumber == 0:
            return what
        if expectNumber < 0:
            return what
        self.helper(root,expectNumber - root.val)

至于列表怎么操作，有想过helper那里加点参数，用来放list,但是感觉又怕操作错误哈哈

答案：
1.递归：
    在expectednum == 0, 且root.left root.right == None 的时候结束：
因为到这里了说明已经遍历到底且找完数字了
    在存在 root.left 和 root.right 的时候继续递归
    
2.数组的处理
    把res = []放在主函数里，然后helper需要一个记录path的列表和res，当记录完毕，加进res之中
    
3.expectednumber的处理，用一个self.sum变量赋值，然后在任何函数里都可以随时访问
    

"""

