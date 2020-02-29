class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            #关键
            res.append([node.val for node in queue])

            level = []
            # 注意我们这里的第二个for循环，就是要把queue给掏空，把下一层
            # 的所有node都放到level里面去。
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            queue = level
        return res




"""
这种每层都记录在一个list里，和单纯按一定顺序全部弄到一个list挺不一样的

应该每一层都要用一个list来记录所有的node.当一次循环结束以后
就进入下一层
那么这个循环应该以怎样的形式开始和结束呢？

答案：
#关键
res.append([node.val for node in queue])
然后我们再用一个for循环来跑这个queue，一次性解决一层所有node
就不像上一题，是每循环一次从容器里拿一个node出来跑
"""
