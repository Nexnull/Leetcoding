class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        res = []
        def preOrder(root):
            if not root:
                res.append('#')
            else:
                res.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(res),len(res)
        #出来的字符串是 "# 1 2 3"，是带空格的


    def Deserialize(self, s):
        chars = [char for char in s.split()]

        def deReOrder():
            if chars:
                char = chars.pop(0)
                if char == "#":
                    return None
                root = TreeNode(int(char))
                root.left = deReOrder()
                root.right = deReOrder()
                return root

        return deReOrder()

"""
这题非常有代表性，记录了如何使用先序遍历，和如何构造回先序遍历
记忆

还有那个res = [] 和内置函数的设定是非常巧妙的，使得每次添加元素都能加进res里面，res也不会被刷新
其实我二刷的时候用的self.list原理也是一样的，一样可以用


"""

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
    print(solution.Serialize(node5))