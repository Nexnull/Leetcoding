class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)

        #在子数组 array[i..j] 中，我们要求的子序列（最长回文子序列）的长度为 dp[i][j]
        dp = [[0 for j in range(l)] for i in range(l)]

        # 每个字符自己都是一个回文子串
        for i in range(l):
            dp[i][i] = 1

        # 每次循环我们都以i为中心点向外扩散
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l, 1):
                # 当i,j相等，那我们就要比较内圈是否相等，如果相等则累加
                # i i+1  j-1 j
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2

                # 当i,j不相等，我们就把当前序列的最大回文串取子串的最大值
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]

"""
https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zi-xu-lie-wen-ti-tong-yong-si-lu-zui-chang-hui-wen/
"""