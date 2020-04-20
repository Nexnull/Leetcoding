class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        seen = {}

        while N > 0:
            c = tuple(cells)
            if c in seen:
                # 例如输入100， N = 85， seen[c] = 88, N = 14
                # print(N, seen[c], seen[c] - N)

                # 假如说c 存在于seen里，那么说明 seen[c]对应的值是比较前期的N
                # 进入这个判断，说明 新c == 旧c，那么 旧N - 新N = 经历多少次是一个循环
                # N % 循环数 = 循环数上所对应的N
                N %= seen[c] - N

            seen[c] = N

            if N > 0:
                N -= 1
                cells = self.nextday(cells)

        return cells

    def nextday(self, cells):
        # 在这里根据上一次的监狱来 推断出下一次监狱是什么样子的
        # 首先第一个牢房和最后一个牢房，只有一个邻居牢房，所以经过一次迭代以后，都会编程0
        # 其次要看当前牢房是否满足题目条件， 那就是 左右牢房是0或者1时， 下一次的中间牢房才是1， 否则就是0
        return [int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1]) for i in range(8)]

"""
思路：https://www.youtube.com/watch?v=iu_45JvAGlw
代码：https://leetcode-cn.com/problems/prison-cells-after-n-days/solution/n-tian-hou-de-lao-fang-by-leetcode/
时间复杂度：O(2^N)，其中 N 是监狱房间的个数。
空间复杂度：O(2^N * N)

这题的两个点：
1。如何推出下一天的监狱
2。如何得出一个循环次数，来进行剪枝

"""