class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def pre(node):
        if node == None:
            return
        print(node.val)
        pre(node.left)
        pre(node.right)


    def preOrder(root):
        if root == None:
            return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop(-1)
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result


    def inorder(node):
        if node == None:
            return
        pre(node.left)
        print(node.val)
        pre(node.right)


    def postorder(node):
        if node == None:
            return
        pre(node.left)
        pre(node.right)
        print(node.val)



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
        pre(node5)
        print(preOrder(node5))