"""
Given a string s, you are allowed to convert it to a palindrome
by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.
在原有的字符串上加点 新char,使整个字符串变成一个回文字符串
Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
