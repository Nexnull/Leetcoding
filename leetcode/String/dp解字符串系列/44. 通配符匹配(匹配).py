class Solution:
    def isMatch(self, s, p):
        ls = len(s)
        lp = len(p)

        # dp[i][j] 代表的是 从0 ~i-1 和 从0 ～ j-1 这两个字符串是否匹配
        # 长度+1的原因是，留空字符进行匹配， 例如 "" 与 "abc"
        # 如果不+1的话，那么就没有空字符匹配了，因为每一个index都对应着一个字母
        dp = [[False for j in range(lp+1)] for i in range(ls+1)]

        # "" "" 是匹配的
        dp[0][0] = True

        for j in range(1,lp+1):
            # 这种情况是 "" 与 "****" 的初始化， 我们要看之前的一位是否为*（看是否为True）
            # 如果为* 且下一位也为*
            # 那么说明可以继承之前的匹配（True), 否则则为False
            dp[0][j] = dp[0][j-1] and p[j-1] == "*"


        for i in range(1,ls+1):
            for j in range(1,lp+1):
                # 如果两个字符串的第 i, j位相同， 那么dp[i][j] 就取决于前面的串是否相同
                # 如果第p[i]位是?，那么说明当前i,j必相同，那么dp[i][j] 就取决于前面的串是否相同
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]

                # dp[i][j - 1]表示 * 代表的是空字符，例如ab, ab *
                # dp[i - 1][j]表示 * 代表的是非空字符，例如 abc, ab*
                # 我们要确保ab ab是匹配的，对于i

                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]


        return dp[-1][-1]

"""
https://leetcode-cn.com/problems/wildcard-matching/solution/dong-tai-gui-hua-dai-zhu-shi-by-tangweiqun/
"""