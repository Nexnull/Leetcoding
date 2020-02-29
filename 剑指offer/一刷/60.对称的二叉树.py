# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.helper(pRoot.left, pRoot.right)

    def helper(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.helper(left.left,right.right) and self.helper(left.right , right.left)
        return False





"""
想到的一种做法就是
把树的每一层都遍历下来，然后在从最左和最右开始向中间遍历


答案：
这种做法是不对的，按照剑指offer的说法
树的正规遍历方法一般是有三种遍历方法，例如前序遍历法 为 前root后
我们可以创造一种镜像前序遍历法， 为后root前
同时一路上保留空节点，把他们都储存在一个list里来比较

然后还有一种做法就是直接用递归来判断；
左树 == 右树， 左树左 == 右树右， 右树左==左树右
做个递归


"""