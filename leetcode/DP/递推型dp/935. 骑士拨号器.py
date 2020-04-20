class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 10**9 + 7

        # 在国际象棋里面，骑士只能走日字型，所以我们一开始就规定了八个方向给它走
        dirs = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

        # 画出我们的棋盘
        dp = [[1 for j in range(3)] for i in range(4)]

        # 把左下和右下的棋盘设为0，因为那两个地方到不了
        dp[3][0] = dp[3][2] = 0

        for k in range(1, N):
            temp = [[0 for j in range(3)] for i in range(4)]

            for i in range(4):
                for j in range(3):
                    # 走到了不可以走的两个位置，跳过
                    if i == 3 and j != 1:
                        continue

                    # 从当前xy出发，能到达的点txty
                    for d in range(8):
                        tx = j + dirs[d][0]
                        ty = i + dirs[d][1]

                        # txty越界处理
                        if tx < 0 or ty < 0 or tx >= 3 or ty >= 4:
                            continue

                        # 时刻注意防止数字越界
                        temp[i][j] = (temp[i][j] + dp[ty][tx]) % mod

            # 最后把这一轮的temp的值全部更新到dp上，为下一轮的temp刷新做准备
            dp = temp[:]

        res = 0
        for i in range(4):
            for j in range(3):
                # 再一次防止越界
                res = (res + dp[i][j]) % mod
        return res

"""
https://www.youtube.com/watch?v=HTnIFivp0aw
"""
