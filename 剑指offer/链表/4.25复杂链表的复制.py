"""
复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None

        currentNode = pHead
        # 1、复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
        # current -> clone -> current.next(nextnode) A->A'->B
        while currentNode:
            cloneNode = RandomListNode(currentNode.label)
            nextNode = currentNode.next
            currentNode.next = cloneNode
            cloneNode.next = nextNode
            #把cur移到下一个node
            currentNode = nextNode

        # 2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next
        currentNode = pHead
        while currentNode:

            if currentNode.random == None:
                currentNode.next.random = None
            else:
                #例如A.random = c 那么我们要做到A'.random = c.next = c'
                currentNode.next.random = currentNode.random.next

            #把cur 移到一下一个currentnode
            currentNode = currentNode.next.next


        # 3、拆分链表，将链表拆分为原链表和复制后的链表
        currentNode = pHead
        pCloneHead = pHead.next
        while currentNode:
            cloneNode = currentNode.next
            currentNode.next = cloneNode.next

            if cloneNode.next == None:
                cloneNode.next = None
            else:
                cloneNode.next = cloneNode.next.next

            currentNode = currentNode.next

        return pCloneHead

"""
https://www.nowcoder.com/profile/2396500/codeBookDetail?submissionId=18667115
还是有点搞不懂为什么需要：
 if cloneNode.next == None:
                cloneNode.next = None
            else:
                cloneNode.next = cloneNode.next.next
这种if,else分开来写？


*解题思路：
*1、遍历链表，复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
*2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
*3、拆分链表，将链表拆分为原链表和复制后的链表

"""