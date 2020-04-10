class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        l1 = len(word1)
        l2 = len(word2)

        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]

        for i in range(l1):
            for j in range(l2):
                # 当前位置相等,最长字串长度加一
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                # 当前位置不相等,等于之前最长字串长度
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return l1 + l2 - 2 * dp[-1][-1]


"""
https://www.youtube.com/watch?v=JCOAUQPamrc
这题和1143，最长公共子序列是同一题
我们所要做的就是 先求出最长公共子序列的长度， 然后用两个字符串的总长- 2*最长公共子序列的长
得到我们要删除多少元素才能成为相同子串
"""