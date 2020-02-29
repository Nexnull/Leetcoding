"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip(" ").split(" ")[-1])


"""
答案：
1. strip(" "),能消除字符串前后的空格，例如"  a   " -> "a"
         但是不能消除字符串中间的空格, 例如 "a b" -> "a b"
2.  str.split(str="", num=string.count(str))
    str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num -- 分割次数。默认为 -1, 即分隔所有。
    
    假如说 "".split(" ") -> [""],但len([""]) = 1
        但 "".split() -> []
           "".split("1") -> ['']
           (假如说一个空字符串，然后以一个实际的东西去分割，那么隔不出东西
           但还是会把""放进[]里去)
           
        
"""