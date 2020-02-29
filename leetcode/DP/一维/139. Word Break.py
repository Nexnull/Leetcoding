"""

"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1]

"""
// Time: O(n^2), Space: O(n+m)
https://algocasts.io/episodes/Z5mzgJGd
https://leetcode.com/problems/word-break/discuss/43995/A-Simple-Python-DP-solution
答案：
1.这题dp的做法有点特别
2.dp[i]表示，从上一个true的未知，到i的位置，这个串，是否在字典里面
3.dp[i] = True，同时表示着，以当前i为字母的开头，能否找到[i，j],存在于字符串里面
例子    l e e t c o d e    {"leet","code"}
dp      t f f f t f f f t  (dp[i] = True每一个都刚好压在字典里每个单词的开始，导致每个单词
                            都可以被找到，return dp[-1]时为True）

反例     l e e t c o d e    {"leetc","code"}
         t f f f f t f f f (因为第一个单词把结尾T放在了O上，导致了第二个code根本无法找到
                            所以dp[-1] = False)

"""