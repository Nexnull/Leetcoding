class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1:
            return False
        if not pRoot2:
            return False

        return self.SubtreeHelper(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)


    def SubtreeHelper(self,pRoot1, pRoot2):
        if pRoot2 == None:
            return True
            #root2已经找完，但没错，说明b树在a树里
        if pRoot1 == None or pRoot1.val != pRoot2.val:
            return False
            #root1已经找完，或者是node的值并不相等，说明b树不在a树里

        #最后就是继续一直往下找在找
        return self.SubtreeHelper(pRoot1.left,pRoot2.left) and self.SubtreeHelper(pRoot1.right,pRoot2.right)


print()



if __name__ == "__main__":
    solution = Solution()

"""
这个做法有缺陷，只能找到子树的root节点，在大树的 root,root.left 或root.right上
要看572的写法，那才是正确的

"""