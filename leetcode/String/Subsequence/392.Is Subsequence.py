"""
Given a string s and a string t, check if s is subsequence of t.

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
顺序得相同，但是不一定要是连续的，例如acd 是 abcd的subsequence
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:return True
        if len(t) == 0:return False
        i , j = 0 , 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False

"""
Time:O(n) space:O(1)
答案：
1.运用了双指针，一个指向s,一个指向t

"""