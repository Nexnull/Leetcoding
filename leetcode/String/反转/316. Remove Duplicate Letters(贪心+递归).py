"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0: return ""

        count = [0]*26
        for char in s:
            count[ord(char) - ord("a")] += 1

        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]: pos = i
            count[ord(s[i]) - ord("a")] -= 1
            if count[ord(s[i]) - ord("a")] == 0:break

        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos],""))

"""
答案：

"""