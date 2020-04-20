class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # 骑士所能移动的八个坐标
        dirs = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

        # 画出我们的棋盘
        dp = [[0.0 for j in range(N)] for i in range(N)]

        # 把当前骑士所在的位置标记成1
        dp[r][c] = 1.0

        for k in range(K):
            temp = [[0.0 for j in range(N)] for i in range(N)]

            for i in range(N):
                for j in range(N):
                    # 从当前xy出发，能到达的点txty
                    for d in range(8):
                        tx = j + dirs[d][0]
                        ty = i + dirs[d][1]

                        # txty越界处理
                        if tx < 0 or ty < 0 or tx >= N or ty >= N:
                            continue

                        # 当前的移动位置后的次数，原来的坐标次数
                        temp[ty][tx] += dp[i][j]

            # 最后把这一轮的temp的值全部更新到dp上，为下一轮的temp刷新做准备
            dp = temp[:]

        res = 0
        for i in range(N):
            for j in range(N):
                # 再一次防止越界
                res += dp[i][j]

        # 因为我们要走K次，然后每次我们都可以走八个方向，所以总的次数是 8**K的次方
        # 其中 在棋盘上的次数是res 次
        # 所以相除就是概率
        return res / 8 ** K

"""
Time: ( k * N^2)  space: N^2
https://www.youtube.com/watch?v=MyJvMydR2G4
"""