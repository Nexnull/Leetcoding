"""
判断是是否为回文数字，12321 可以 ， -121 ！= 121-不可以
0 可以
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        temp = x
        res = 0
        while temp > 0:
            res = res * 10 + temp % 10
            temp /= 10

        return res == x

"""
这题其实跟7,reverse integer很像
// Time: O(m), Space: O(1)
https://algocasts.io/episodes/zbmKMpZq
答案：
1.我们已知负数是一定不行的，所以x<0,return false
2.我们用res来计算x的相反数字
3.res*10等于把原来有的数进位，9 -> 90, + temp%10,把temp最末尾一位加到res
4.return时对比两者是否相同

答案2：
可以用双指针，但是TimeO(n) space:O(n)
"""