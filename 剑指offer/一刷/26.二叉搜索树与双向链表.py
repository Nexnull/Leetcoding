"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        self.linkedlistLast = None
        self.helper(pRootOfTree)
        pHead = self.linkedlistLast
        while pHead and pHead.left:
            pHead = pHead.left
        return pHead

    def helper(self,node):
        if not node:
            return
        cur = node

        self.helper(cur.left)

        #此时cur已经是最左节点了,同时也是中序遍历到新节点，所以应该把cur.left 设为self.linkedlistLast
        cur.left = self.linkedlistLast
        #让linedlistLast 与cur相连，因为上面是cur 连self.linkedlistLast
        if self.linkedlistLast:
            self.linkedlistLast.right = cur

        #让cur成为新的 self.linkedlistlast,因为我们已经把当前的cur跟链表连好了
        self.linkedlistLast = cur

        #继续中序遍历
        self.helper(cur.right)


"""
排序的双向链表吗
要做到排序的标准的话，只能用中序遍历，这样在BST中它才是排好序的
然后呢？

答案：
1.设定变量self.linkedlistLast = None
它的作用是每次存放当前遍历的节点，且在下一次循环中，把它作为下一个节点
的左节点（因为遵循中序遍历，所以每一次的node总是大于上一个node）
2.其实做的操作就是，


"""