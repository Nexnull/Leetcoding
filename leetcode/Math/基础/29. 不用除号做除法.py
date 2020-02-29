"""
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0): sign = -1
        dividend, divisor, res= abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i += i
                temp += temp


        return min(max(-2147483648, res*sign), 2147483647)

"""
答案：time O(logn), space(1)
https://www.youtube.com/watch?v=XKuFGEGt5zo
0.这题我们并不需要判断corner case
1.一开始我们先判断符号
2.初始化各种值，把他们的符号都去掉
3.当被除数 >= 除数时
4.例如 9 / 2, end = 9, or = 2 , temp = 2 , i = 1
5.while 9 > 2, (while 等于是一种加速，加快计算进度，其实不这样写也是可以的）
    end -= temp(2) ->7
    res + i
    i  <<= 1 (等于乘2)
    temp <<= 1(temp乘2)
    
因为我们试图返回的是 9 = 2*(2^2) 返回2^2, i为2的倍数
6.假如说 9 < 16,那么则退出到第一个for循环，temp,i再次 = 1，继续5的操作

"""
