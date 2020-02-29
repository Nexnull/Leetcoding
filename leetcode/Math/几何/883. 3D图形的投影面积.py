"""
6 2
3 4

[6,4] 相同j,的最大值 [?][j]
[6,4] 相同
"""
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        area = 0

        for i in range(len(grid)):
            front = 0
            side = 0
            for j in range(len(grid[0])):
                # 俯视图
                if grid[i][j]: area += 1
                # 前视图
                front = max(front, grid[j][i])
                # 左视图
                side = max(side, grid[i][j])

            area += front + side
        return area

"""
leetcode原题答案
答案：
投影面积总共有三部分构成：俯视图，左视图，前视图
俯视图就要看当前位置上有没有柱子，有柱子的话就+1
前视图，我们是一次i,遍历一次col,找到这个col的最大值
左视图，我们是一次i,遍历一次row,找到这个row的最大值
"""