class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 == None or s2 == None or s3 == None:
            return False

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        # 长度都匹配不到一起，自然不可能由s1 s2构成
        if l1 + l2 != l3:
            return False

        dp = [[[False for k in range(l3 + 1)] for j in range(l2 + 1)] for i in range(l1 + 1)]

        # 初始化, 两个长度为空的字符串肯定能 组成另一个长度为空的字符串
        dp[0][0][0] = True

        # 把能初始化的都初始化
        for i in range(1, l1 + 1):
            dp[i][0][i] = dp[i - 1][0][i - 1] and s1[i - 1] == s3[i - 1]
        for j in range(1, l2 + 1):
            dp[0][j][j] = dp[0][j - 1][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                k = i + j
                # 看看是否满足递推条件
                dp[i][j][k] = (dp[i - 1][j][k - 1] and s1[i - 1] == s3[k - 1]) or (
                            dp[i][j - 1][k - 1] and s2[j - 1] == s3[k - 1])

        return dp[-1][-1][-1]

"""
https://algocasts.io/episodes/LPmwE7pq
Time: O(n1*n2), Space: O(n1*n2*n3)

dp[i][j][k]的含义是，用s1的i个字符 和 s2的j个字符能交替合并成 s3的k个字符

我们看s1,s2能不能拼成s3
看dp[i - 1][j][k - 1]能不能拼成 s3 的0 - k-1, 然后再看s1[i]和 s3[k]相不相等，相等则能拼成
dp[i][j][k] = dp[i - 1][j][k - 1] and s1[i - 1] == s3[k - 1]

看dp[i][j - 1][k - 1]能不能拼成 s3 的0 - k-1, 然后再看s2[j]和 s3[k]相不相等，相等则能拼成
dp[i][j][k] = dp[i][j - 1][k - 1] and s2[j - 1] == s3[k - 1]
"""