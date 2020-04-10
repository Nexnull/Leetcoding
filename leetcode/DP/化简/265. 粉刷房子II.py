import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])

        # k colors and n houses
        dp = [[0] * k for _ in range(n)]

        for i in range(k):
            dp[0][i] = costs[0][i]

        for i in range(1, n):
            # [i][j] is current dp, we need to update it
            for j in range(k):
                # using minum to memo the min value in [i][0-j]
                minum = sys.maxsize
                for c in range(k):
                    if j != c:
                        minum = min(minum, dp[i - 1][c])
                dp[i][j] = minum + costs[i][j]

        # [-1]包括了 dp[-1][0,1,2],我们把它其中的最小值找出来就好了
        return min(dp[-1])


"""
// Time: O(n*k^2), Space: O(n*k)
https://algocasts.io/episodes/VlWdLOW0
思路与粉刷房子1基本一样，这里不考虑各种优化的写法
"""