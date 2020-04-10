"""
写一个支持加减乘除的计算器
使得给出一个字符串，它能计算出里面的数值
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0: return 0

        res = 0
        op = "+"
        part = 0
        p = 0

        while p < len(s):
            while s[p] == " ":
                p += 1
            num = 0
            while p < len(s) and "0" <= s[p] <= "9":
                num = num*10 + (ord(s[p]) - ord("0"))
                p += 1

            if op == "+":
                res += part
                part = num
            elif op == "-":
                res -= part
                part = num
            elif op == "*":
                part *= num
            elif op == "/":
                part /= num

            while p < len(s) and s[p] == " ": p += 1
            if p < len(s):
                op = s[p]
                p += 1
        return res + part


