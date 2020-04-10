class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        l1 = len(s1)
        l2 = len(s2)
        ascii_sum = sum([ord(s) for s in s1]) + sum([ord(s) for s in s2])

        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]

        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return ascii_sum - 2 * dp[-1][-1]
