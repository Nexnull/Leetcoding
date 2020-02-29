class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        res = []
        if not root:
            return []

        queue = [root]

        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(res)


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

"""
这是顺序打印二叉树，主要要制造一个容齐来存放node,然后用另外一个容器来
存放结果

"""