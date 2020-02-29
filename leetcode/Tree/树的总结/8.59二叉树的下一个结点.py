"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, node):
        if node == None:
            return None

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            while node.next:
                if node.next.left == node:
                    return node.next
                if node.next.right == node:
                    while node.next:
                        if node.next.left == node:
                            return node.next
                        node = node.next

        return None









"""
中序遍历：left , root , right
问题：
怎么知道该节点的下一个是左节点还是右节点还是root呢?

答案：
首先要记住的是，各种遍历法都是，中序遍历法，永远是左者优先，就是实在没左了，才中，最后才右

1。首先判断node是否存在

2。node存在右节点，
  2。1假如说只有一个右节点，则只返回这个右节点
  2。2假如这个右节点存在左节点，则从node的右节点出发，一直向左找，找到尽头的那一个就是

3。node不存在右节点（不是根节点），该node也不存在左节点，就是一个孤零零的node，
    3。1 该node是node.next的左子树
    下一个节点应该返回node的父节点（因为left已经走完了，要回到root)
    3.2 该node是node.next的右子树，那么应该一直向上找，直到找到一个node 是在node.next.left
    那么这个node.next就是我们需要的节点
    
关于第三点怎么用代码实现：
                while pNode.next:
                    if pNode == pNode.next.left:
                        return pNode.next
                    pNode = pNode.next
其实关键点都是在，返回父节点，我自己的一个写法，写的就比较清楚：
                while node.next:
                    if node.next.left == node:
                        return node.next
                    if node.next.right == node:
                        while node.next:
                            if node.next.left == node:
                                return node.next
                            node = node.next
    
remark:
    为什么没出现，node存在左节点的情况。因为我们知道，最左的一定是最早被遍历的
    所以即使是node存在左节点，那么node.left也一定是被遍历过了，就只剩下node.right没被遍历了
    （因为root就是当前节点）
    所以换而言之，我们只需要讨论node有没有右节点这两种情况



"""