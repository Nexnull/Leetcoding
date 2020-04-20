"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:
Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""

class Solution(object):
    # 暴力解法，强行把每个数字都算1
    # Time: O(n*log10(n)), Space: O(1)
    def countDigitOneBruteForce(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        count = 0
        for i in range(1,n+1):
            num = i
            while num != 0:
                if num % 10 == 1:count += 1
                num /= 10
        return count

    def countDigitOneMath(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        count = 0
        factot = 1
        while n / factot != 0:
            digit = (n/factot) % 10
            high = n / (10*factot)
            if digit == 0:
                count += high*factot
            elif digit == 1:
                count += high*factot
                count += (n%factot)+1
            else:
                count += (high+1)*factot

            factot *= 10
        return count



"""
Time: O(log10(n)), Space: O(1)
假设12345
factor = 1,10,100,10000,10000
count 表示当前factor,1的数量
digit 当前锁定的数，个十百千万，这样一位一位地向上锁
high  比digit位数高的数，例如digit是百位，high就是千万位（high high d low low）
low   我们用 n%factor + 1表示，例如45,他是从00 - 45，共有46个数字

三种情况：
digit = 0:  _ _ 0 _ _ 12034
这时简单，直接把high(12)*factor(100), 因为我们只计算百位的含1数，百位只能出现1次1
                                    所以1 _ _ , _ _ = 【0，99]，所以锁定百位
                                    能出现100个1。 然后我们有12个100

digit = 1:  _ _ 1 _ _ 12134
直接把high(12)*factor(100) + low + 1,计算百位的方法与上同理，所以有12 * 100
                                    但是我们这里的digit是1，所以还要把1 _ _
                                    这种情况考虑进去，就是 low = [00,34],35个数

digit = 1:  _ _ 3 _ _ 12134
直接把(high(12)+1)*factor(100)      ,计算百位的方法与上同理，所以有12 * 100
                                    但是我们这里的digit>1，所以还要把1 _ _
                                    所以12100-12199我们也遍历完了，所以等于还要再
                                    +100,于是化简成 (high+1) * factor
                                    
"""



