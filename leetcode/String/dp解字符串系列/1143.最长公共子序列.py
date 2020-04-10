"""
Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
找出字符串1和2的最长相同子序列是多长（不要求连续）->例1
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2: return 0

        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]


"""
https://www.youtube.com/watch?v=Dumq-rceuac
答案：
1. 我们得把这两个字符串，一个放在横轴，一个放在纵轴，dp就是这个矩阵，用来记录当前横纵坐标上的最大递增子序列
2.  _ a b c d e
  _ 0
  a 
  c
  e

我们最好把dp构造得比原数组都长一位，这样方便操作
假如 [i] == [j], 例如 ab ab, 那dp[i][j] = dp[i-1][j-1] + 1 等于 a + 1
假如 [i] != [j], 例如 ab ac, 那么我们就看 max( ab,a  和 a,ac) 看之前这两段，哪段的公共子序列更长，把它更新上去
"""