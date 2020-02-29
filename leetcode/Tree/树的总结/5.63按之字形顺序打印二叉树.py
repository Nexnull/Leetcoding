class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, root):
        if not root:
            return []

        res = []
        queue = [root]
        flag = True

        while queue:
            # 用一个flag来判断结果加进数组的顺序
            if flag == True:
                 res.append([node.val for node in queue])
                 flag = False
            else:
                res.append([node.val for node in queue][::-1])
                flag = True

            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp

        return res




"""
（源自第三题的做法）
这题我还有印象，我的之前的做法是，用两个容器来存放node,一个存正序，一个存倒序
然后用一个标志来判断，到底是存正序还是存倒序
当遍历正序node的时候，就应该按倒序来存
当遍历倒序node的时候，就应该按正序来存

看了下网上的做法，感觉思路上是差不多的，但是其实这题可以用一个容器做
（源自第四题的做法）
可以利用第四题的把二叉树打印成多行的方法来做，只是在append进res之前
先要做一次判断要不要进行reverse
"""