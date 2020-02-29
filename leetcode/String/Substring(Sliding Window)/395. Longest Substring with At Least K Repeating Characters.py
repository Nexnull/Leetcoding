"""
找出一个字符串T的最长连续子字符串，要求这个子字符串中每个字符出现的次数都最少为K，
求出这个子字符串的最长长度。
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        for char in set(s):
            if s.count(char) < k:
                return max([self.longestSubstring(div,k) for div in s.split(char)])
        return len(s)

"""
https://blog.csdn.net/fuxuemingzhu/article/details/82889933
答案：
1.如果字符串s的长度少于k，那么一定不存在满足题意的子字符串，返回0；
2.如果一个字符在s中出现的次数少于k次，那么所有的包含这个字符的子字符串都不能满足题意。所以，应该去不包含这个字符的子字符串继续寻找。这就是分而治之的思路，返回不同子串的长度最大值。
3.如果s中的每个字符出现的次数都大于k次，那么s就是我们要求的字符串。

"""