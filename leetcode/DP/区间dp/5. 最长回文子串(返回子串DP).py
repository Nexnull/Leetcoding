class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = len(s)
        maxLen = 0
        start = 0

        dp = [[False for j in range(l)] for i in range(l)]

        for i in range(l - 1, -1, -1):
            for j in range(i, l, 1):
                #初始化出现奇数的情况， 例如 bab
                if i == j:
                    dp[i][j] = True

                #初始化出现偶数的情况， 例如 baab
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]

                # 解决通用情况，i i+1 j-1 j
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                # 当最长子串更新以后，记得回来更新maxLen 和start
                if dp[i][j] and (j - i + 1) > maxLen:
                    maxLen = j - i + 1
                    start = i

        return s[start: start + maxLen]


"""
Time: O(n^2), Space: O(n^2)
https://algocasts.io/episodes/VBpLqWD8
"""