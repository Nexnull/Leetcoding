"""
Given a non-empty array of digits representing a non-negative
 integer, plus one to the integer.
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits or len(digits) == 0:
            return [1]

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits[0] = 1
        digits.append(0)
        return digits

"""
time:On space O1
https://www.youtube.com/watch?v=6A-DTVB9HT8
答案：
0.遇到这种涉及加法的题，我们需要从后往前遍历
1.[4,1,1,1]正常情况就返回[4,1,1,2]就好
2.例如[4,1,1,9],遍历到9的时候变0，遍历到1的时候+1
3.例如[9,9,9,9],遍历完所有，[0,0,0,0]，然后使得第一位变成1，[0]=1,
然后补上最后一位append(0),[1,0,0,0,0]
"""

#自己的另一种写法
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]

        up = 0
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            #每一次我们都查看digits[i] + up 是否=10，如果为10，那么吧digits[i]
            #变成0， 然后up = 1,进入下一次循环
            if digits[i] + up == 10:
                digits[i] = 0
                up = 1
            #假如说是正常的数字（非9)
            else:
                #假如说上一位有进1，我们就在这里给加上
                if up == 1:
                    digits[i] += 1
                #没有进位就不用管了
                #进位处理完都清0
                up = 0

        #这是[9,9,9]的情况，循环结束以后变成[0,0,0] up=1,然后我们把它加到最前面就好
        if up == 1:
            digits.insert(0, 1)

        return digits