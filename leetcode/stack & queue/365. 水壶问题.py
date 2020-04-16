class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        stack = [(0, 0)]
        self.seen = set()

        while stack:
            remain_x, remain_y = stack.pop()

            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in self.seen:
                continue

            # 检查完后,我们开始进行新一轮的设定
            self.seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))

            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(y - remain_y, remain_x),
                          (remain_y + min(y - remain_y, remain_x))))

            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x),
                          remain_y - min(remain_y, x - remain_x)))

        return False

"""
时间复杂度 o(XY) 状态数有（X+1)(y+1)种， 对每种状态进行深度优先搜索，时间复杂度为O（1）
空间复杂度为O（XY), 也是应为状态数有（X+1)(y+1)，所以set里最多有（X+1)(y+1)
这题非常好玩
链接：https://leetcode-cn.com/problems/water-and-jug-problem/solution/shui-hu-wen-ti-by-leetcode-solution/
首先对题目进行建模。观察题目可知，在任意一个时刻，此问题的状态可以由两个数字决定：X 壶中的水量，以及 Y 壶中的水量。

在任意一个时刻，我们可以且仅可以采取以下几种操作：

把 X 壶的水灌进 Y 壶，直至灌满或倒空；
把 Y 壶的水灌进 X 壶，直至灌满或倒空；
把 X 壶灌满；
把 Y 壶灌满；
把 X 壶倒空；
把 Y 壶倒空。

搜索中的每一步以 remain_x, remain_y 作为状态，即表示 X 壶和 Y 壶中的水量。
在每一步搜索时，我们会依次尝试所有的操作，递归地搜索下去。这可能会导致我们陷入无止境的递归
因此我们还需要使用一个哈希结合（HashSet）存储所有已经搜索过的 remain_x, remain_y 状态
保证每个状态至多只被搜索一次。

"""