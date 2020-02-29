"""
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来
的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。



"""



# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.string = ""
        self.list = []

    def Serialize(self, root):

        def se_helper(root):
            if root == None:
                self.list.append("#")
            else:
                self.list.append(str(root.val))
                se_helper(root.left)
                se_helper(root.right)
        se_helper(root)
        return "".join(self.list)



    def Deserialize(self, s):
        s = list(s)

        def de_helper():
            if s:
                node_val = s.pop(0)
                if node_val== "#":
                    return None
                else:
                    root = TreeNode(int(node_val))
                    root.left = de_helper()
                    root.right = de_helper()
                    return root

        return de_helper()



"""
写到serialize时
感觉还行，但是把它从字符串变回去，因为我写的时中序遍历，然后参数只能传一个字符串
就在想是不是每次都要用个for 循环把root找出来

并不用，这里巧妙的利用了递归来分解这个node列表



还有一个问题，这样重排，递归是怎么知道哪个点到root.left,什么时候到root.right了啊？

在递归中，如果遇到"#"，返回None,那么这个条线就直接结束了
例如一直向左递归，递归到#了，说明node.left已经是没有东西了
因为node.left已经被找完了，那么按照先序遍历的规律
就要就执行root.right（）的递归了。

还有一个小bug,假如说出现有二位数，那么就不能用我这个list(s)了，因为两位数会被拆分成两个数
导致很多出错，所以一刷的那个答案考虑的是非常充分的，利用split()来分隔开每个数

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
    # print(solution.Serialize(node5))
    print(solution.Serialize(solution.Deserialize("5421##3###6#87###")))