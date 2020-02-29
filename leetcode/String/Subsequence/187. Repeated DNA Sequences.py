"""
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

题目大意
在一个字符串中找出连续的十个字符，这十个字符不止在一个地方出现过。

原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/83017233
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s < 10: return []

        seen = set()
        repeat = set()

        for i in range(len(s) - 9):
            temp = s[i:i + 10]
            if temp in seen:
                repeat.add(temp)
            else:
                seen.add(temp)
        return list(repeat)
"""
time O(n) Space O(n)
答案：
hash set来解, 有个位运算的解法，懒得学
1.我们每次把字符串都切割成一个长度为10的字串
2.假如说我们第一次看到这个字串，那就把它加进seen里
3.假如这个字串出现了不止一次，那我们要把这个字串加进repeat里
4.最后我们把repeat给按照格式输出就好了
"""