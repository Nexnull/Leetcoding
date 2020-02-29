"""
Given a string, determine if it is a palindrome,
considering only alphanumeric（数字和字母） characters and ignoring cases（忽略大小写）.
"""


class Solution(object):
    def is_alphanumeric(self, char):
        return ("a" <= char <= "z") or \
               ("A" <= char <= "Z") or \
               ("0" <= char <= "9")

    def is_ignoring_case(self, a, b):
        if "a" <= a <= "z": a = chr(ord(a) - 32)
        if "a" <= b <= "z": b = chr(ord(b) - 32)
        return a == b

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0: return True
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not self.is_alphanumeric(s[i]):
                i += 1
            while i < j and not self.is_alphanumeric(s[j]):
                j -= 1

            if i < j and not self.is_ignoring_case(s[i], s[j]):
                return False
            i += 1
            j -= 1

        return True

"""
https://algocasts.io/episodes/4rpaqpZb
Time: O(n), Space: O(1)
ord("")返回它对应的ascii数，chr()把ascii转换成字符串
答案：
1.is_alphanumeric用于检测char是否满足题目要求的alphanumeric
2.is_ignoring_case用于检验字母是否回文（自动转换为大写用于比较）
3.双指针，左右同时向中间检查，满足条件return
"""
