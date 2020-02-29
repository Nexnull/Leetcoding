class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def PrintFromTopToBottom(self, root):
    # write code here
    l = []
    if not root:
        return []
    q = [root]
    while len(q):
        t = q.pop(0)
        l.append(t.val)
        if t.left:
            q.append(t.left)
        if t.right:
            q.append(t.right)
    return l




"""
当年写leetcode对这种层状树结构非常熟练，奈何时间太久忘记了
我这种写法应该是正确的，问题是答案给的接口太傻逼了，下面po答案吧

这一看就知道是错了，因为假如说一直存在root.left,那么就会一直往root.left
遍历，直到root.left遍历完了

答案使用队列来实现的，把每一个node放进去，然后对这个node的左右都探查一边，探查完了加进列表



"""

