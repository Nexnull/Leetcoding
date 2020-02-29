"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s or not t: return True

        hashmap = {}
        if len(s) != len(t):return False

        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap.get(s[i]) != t[i]:return False
            else:
                if t[i] in hashmap.values():
                    return False
                else:
                    hashmap[s[i]] = t[i]
        return True

"""
Time O(n) space O(n0
https://www.youtube.com/watch?v=tBK5f-BJOdg
答案：
1.我们用hashmap（python 中的dictionary）,来储存 s:t
  例如： abb
        egg  (a:e , b:g) 那么后续碰到a,b这两个字母，我们只用看看value对不对的上就可以了

2.当两个string长度都不一样，肯定不是同构
3. 假如说s[i] 在hashmap里面，那么取出s[i]的value,看和t[i]对不对的上
4. 假如说s[i] 不在hashmap里面，就要看t[i]在不在hashmap.values()里，有的话说明错了
              若都不在，那就把他们两加进map里
5.经过重重考验，最后可以return True了ß


"""













