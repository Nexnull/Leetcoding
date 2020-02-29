"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2: return 0

        m = len(word1)
        n = len(word2)

        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1): dp[i][0] = i
        for j in range(n+1): dp[0][j] = j

        # 检测出"a",""这种情况
        if n == 0 or m == 0: return dp[m][n]

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                               dp[i-1][j] + 1,
                               dp[i][j-1] + 1)

        return dp[m][n]

"""
https://www.youtube.com/watch?v=CikSnHInOJQ&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=52
https://www.youtube.com/watch?v=Q4i_rqON2-E
答案：
1.dp[i][j] i表示word1的0-i的片段，j表示word2的0-j的片段，合在一起的意思就是
word1的0-i的片段 和 word2的0-j的片段，把他们变成相同的字符串需要多少步操作
2.假如说，word1的第i位 和word2的第j位相等，那么就说明在这个index上不用操作
dp[i][j] = dp[i-1][j-1]
3.当i,j位不相等时，我们有三种操作，delect,insert,replace
  其实delect 和 insert 分的不是特别清楚，一个是[i-1][j],一个是[i][j-1]
  replace,把i换成与j相同的字母，然后同时消去这两个字母，所以[i][j] = [i-1][j-1] + 1
  然后我们取这三个操作的最小值（其实就是尝试这三个操作哪个花费最少），用个min

4.注意我们先得把递归的基础值给设定好，利用两个for循环（假如一个单词是""，另一个单词是x）
5.把两个单词的所有情况都遍历一遍，推出最后的dp[m][n]

remark:
注意最后两个for循环是从1开始的，因为中途判断word1[i-1] == word2[j-1],不从1开始会
有index错误， 同时我们直到dp[0][0] = 0 ,[0][1],[1][0]都是有预设值的，所以可以不必
遍历他们


"""