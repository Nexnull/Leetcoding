# -*- coding:utf-8 -*-
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
这题完全没想法，就按照答案讲的学一学把；
https://www.nowcoder.com/profile/2396500/codeBookDetail?submissionId=18667115

*解题思路：
*1、遍历链表，复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
*2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
*3、拆分链表，将链表拆分为原链表和复制后的链表

"""