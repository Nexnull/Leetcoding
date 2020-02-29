class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

number = []
class Solution:
    def TreeDepth(self, pRoot):
        self.helper(pRoot,0)
        return max(number)

    def helper(self, node, length):
        if node == None:
            return number.append(length)
        self.helper(node.left,length+1)
        self.helper(node.right,length+1)

# def main():
#     treenode = TreeNode(1)
#     solution = Solution()
#     print(solution.TreeDepth(treenode))
#     print(111)
#


"""
我的想法：
感觉是不是深度优先，先找出每一条路，然后把记录，一直找
直到找到最长的

关于怎么记录这个最大数，我一时之间想不到很好的办法，只想到放一个globle的array
来记录每条路的长度，最后return max(array)



答案：
"""
class Solution:
    def TreeDeep(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDeep(pRoot.left)
        right = self.TreeDeep(pRoot.right)
        return left + 1 if left > right else right + 1


