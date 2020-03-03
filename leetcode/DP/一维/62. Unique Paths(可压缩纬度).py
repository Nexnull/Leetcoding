
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
m是col，n是row, 机器人每改变一个方向算有加上一种走法
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n < 1 or m < 1: return 0

        dp = [[1 for j in range(n) ] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


"""
 // Time: O(m*n), Space: O(m*n)
https://algocasts.io/episodes/Y9pJQNGA
答案：
1.我们先创建一个m*n 的矩阵，然后把1附值到横竖进去，(但我这里写的是创造了一个全为1的矩阵，因为后面可以覆盖，所以问题不打)
    
    1 1 1 1
    1 0 0 0
    1 0 0 0

因为，机器人只能向下或者向右走，所以机器人光向下走和光向右走都只要一种走法
2. dp[i][j] = dp[i-1][j] + dp[i][j-1] 因为，机器人只能向下或者向右走，所以到达当前这个点
   可能是从上往下走了一步，或者是从左向右走了一步，这一步由前面的两个状态结合而成
"""