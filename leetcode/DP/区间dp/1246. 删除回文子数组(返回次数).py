"""
给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 
arr[i], arr[i+1], ..., arr[j]（ i <= j）。
注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。
请你计算并返回从数组中删除所有数字所需的最少操作次数。

输入：arr = [1,3,4,1,5]
输出：3
解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。
"""
import sys


class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = len(arr)
        # 我们令dp(i,j)代表删除区间[i,j]的最小值（即最小删除次数）
        dp = [[0 for j in range(l)] for i in range(l)]

        # 单个字符也是回文串
        for i in range(l):
            dp[i][i] = 1

        for j in range(1, l):
            for i in range(j - 1, -1, -1):
                # 区间只有两个元素的时候
                if i == j - 1:
                    # 如果i == j, 那么说明这个区间只有一个回文子串
                    # 若不等，则有两个
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                    continue

                # 大于两个元素的时候
                min_pre = sys.maxsize
                if arr[i] == arr[j]:
                    # 头尾相等，最小值有可能是出现在这对头尾最后被删的结果
                    min_pre = dp[i + 1][j - 1]

                # 最关键的在这里，我们等于一遍遍去尝试，看有没有更小的结果
                for k in range(i, j):
                    min_pre = min(min_pre, dp[i][k] + dp[k + 1][j])

                dp[i][j] = min_pre

        return dp[0][-1]

"""
https://leetcode-cn.com/problems/palindrome-removal/solution/java-liang-chong-jie-fa-dp-and-backtrack-by-npe_tl/

我们令dp(i,j)代表删除区间[i,j]的最小值（即最小删除次数）
递推式子：
if a[i] == a[j]:
    min(dp[i+1][j-1], dp[i][k] + dp[k+1][j]) i <= k <= j
if a[i] != a[j]:
    min(dp[i][j], dp[i][k] + dp[k+1][j]) i <= k <= j
    
其中dp[i][k] + dp[k+1][j]是在i,j范围内不断尝试的过程
"""