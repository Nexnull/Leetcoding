class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.jumpFloor(3))

#树的测试案例
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    node5.left = node4
    node5.right = node6

    node4.left = node2
    node2.left = node1
    node2.right = node3

    node6.right = node8
    node8.left = node7
    solution = Solution()
    solution.PrintFromTopToBottom(node5)


if __name__ == "__main__":
    li1 = ListNode(1)
    li2 = ListNode(2)
    li3 = ListNode(3)
    li4 = ListNode(4)
    li5 = ListNode(5)

    li1.next = li2
    li2.next = li3
    li3.next = li4
    li4.next = li5
    solution = Solution()
