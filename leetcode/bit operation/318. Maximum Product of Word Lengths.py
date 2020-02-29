"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters.
You may assume that each word will contain only lower case letters.
If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn"

给你一组字符串组成的列表，让你求里面两个不含相同char的字符串所能组成的最大长度乘积
"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words or len(words) == 0: return 0

        wordmatch = [0] * len(words)

        for i in range(len(words)):
            for j in range(len(words[i])):
                wordmatch[i] |= (1 << ord(words[i][j]) - ord('a'))

        res = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if wordmatch[i] & wordmatch[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
"""
Time O(n^2) space O(n)
答案：
1.这题作为位运算的一题主要的做法是，用wordmatch 去储存第i个字符串 所对应的二进制表
  例如， "abc"的二进制表为 000000000111
  那么，看它与"cde"是否有重复字符 00011100

      00111
    & 11100  
    --------
      00100  != 0,说明有重复字符
      
      wordmatch[i] |= (1 << ord(words[i][j]) - ord('a'))就是用来完成这个的
      
"""