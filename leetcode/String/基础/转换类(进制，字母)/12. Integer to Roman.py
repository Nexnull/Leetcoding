"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. 12 = X(10) + II(2)
The number twenty seven is written as XXVII, which is XX + V + II. 27 = XX(20) + V(5) + II(2)
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = []
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                res.append(strs[i])

        return "".join(res)

"""
https://www.youtube.com/watch?v=pSxbXcCH5no
答案：简单粗暴地找数字，只要找到values[i] 比 num小就立刻把 value[i] 对应地string 放进res去
"""