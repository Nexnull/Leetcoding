"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
从205题的同构字符串，变成290题的同构单词
"""


class Solution(object):
    def wordPattern(self, s, t):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not s or not t: return False

        hashmap = {}
        t = t.split(" ")
        if len(s) != len(t): return False

        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap.get(s[i]) != t[i]: return False
            else:
                if t[i] in hashmap.values():
                    return False
                else:
                    hashmap[s[i]] = t[i]
        return True

"""
Time O(n) space O(n）
看205题就好了
"""