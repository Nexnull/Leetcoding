"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s) - 1
        res = 0
        temp = 1

        for i in range(n, -1, -1):
            res += (ord(s[i]) - ord("A") + 1) * temp
            temp *= 26

        return res

"""
答案：
1. "ABC" =  "A"*26^2 + "B"*26^1 + "C"*26^0
2. 由此可知，我们要从后往前遍历
3. 假如说现在的 我们要求 "A"， 那么(ord("A") - ord("A")) * temp = 0
                            又因为A = 1，所以我们要在里面加上一个1
"""