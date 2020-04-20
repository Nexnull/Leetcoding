"""
Given two strings s and t , write a function to determine
if t is an anagram（相同字母异序词） of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (not s and t) or (not t and s): return False
        alphabet = [0] * 26

        for i in range(len(s)): alphabet[ord(s[i]) - ord("a")] += 1
        for i in range(len(t)): alphabet[ord(t[i]) - ord("a")] -= 1
        for i in alphabet:
            if i != 0: return False
        return True


"""
答案：
可以用hashmap(字典) 来做，两个字典dic1[item] = dic1.get(item, 0) + 1,最后dic1 == dic2
也可以直接 sorted(s) == sorted(t) 来做
以上两种做法：https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).

Time O(n) Space O(n)
最高赞做法：
https://leetcode.com/problems/valid-anagram/discuss/66484/Accepted-Java-O(n)-solution-in-5-lines
1.不是要看这两个字符串是不是由相同数量，相同字母组成的吗，直接创建一个list来统计
2.第一string , 每个字符对应的位置++
3.第二个string,每个字符对应的位置--
4.两个字符串相等的话，那么alphabet应该里面全是0
"""

