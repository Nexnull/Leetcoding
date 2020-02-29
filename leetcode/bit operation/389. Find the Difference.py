"""
给你两个字符串，让你找到里面多出现的一个字符
Input:
s = "abcd"
t = "abcde"
Output:
e
Explanation:
'e' is the letter that was added.
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for char in s + t:
            res ^= ord(char)
        return chr(res)
"""
time O(n), space O(1)
答案：
1. 利用^来做，以下是^的特性
   x ^ x = 0 ; 
   0 ^ x = x;  
   a ^ a ^ x ^ x^ b = b
这题就是剑指offer41的更简单版本，不过从原来的处理数字变成处理字符串
由于int 无法^ str,所以我们得先把str转换成 ord()，然后异或
最后return chr
"""
