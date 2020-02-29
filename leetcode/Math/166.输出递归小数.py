"""
Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

无限循环小数应该这样处理
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        num , den = numerator, denominator
        # 分母为0
        if not den: return
        # 分子为0
        if not num: return "0"

        res = []
        if (num < 0) ^ (den < 0):
            res.append("-")

        num, den = abs(num), abs(den)
        res.append(str(num//den))
        rmd = num % den
        #如果没有余数
        if not rmd:
            return "".join(res)

        #无返回的话说明有余数
        res.append(".")

        dic = {}
        while rmd:
            # 出现循环小数了
            if rmd in dic:
                res.insert(dic[rmd], "(")
                res.append(")")
                break

            dic[rmd] = len(res)
            div = rmd*10 // den
            rmd = rem*10 % den
            res.append(str(div))
        return "".join(res)


"""
思路：https://www.youtube.com/watch?v=WJMrceU-ujs
答案：https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51187/Python-easy-to-understand-solution-with-comments.
答案：

"""