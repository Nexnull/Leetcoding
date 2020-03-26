"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "acba"
输出: True
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # 在 l != r的时候，说明l 或者r 有一个是错误的，所以我们要避开这两者之一，继续往下查找
                # 找得到，就是true,找不到就是false
                return self.helper(s, l + 1, r) or self.helper(s, l, r - 1)
            else:
                l += 1
                r -= 1

        return True

    def helper(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

"""
https://www.youtube.com/watch?v=hvI-rJyG4ik
"""