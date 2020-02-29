"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
"""
#O(n^2) O(1)
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num or num < 0:return 0
        res = 0
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num /= 10
            num = temp
        return num

"""
答案：
这个方法复杂度就比较高一点
1.我们用temp去+= num的每一位数字（num%10)
2.如果temp 加完以后发现>= 10,则num = temp,再重复一次1的操作

这题还有一个O(1)时间的，是个数学规律，(nums-1)%9 + 1就刚好等于值
https://www.youtube.com/watch?v=4AqAgD_RveA&t=275s
"""