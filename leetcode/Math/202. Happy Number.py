"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        repeat_set = set()
        while n != 1:
            n = self.transform(n)

            if n not in repeat_set:
                repeat_set.add(n)
            else:
                return False

        return True

    def transform(self, n):
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n /= 10

        return res

"""
Time: O(1), Space: O(1)
https://algocasts.io/episodes/6emEKnpV
答案：
1.假如我们一直求 位数的平方和，我们知道，只有找到1的时候才能破除循环，但是找不到1的时候，什么情况才是终止条件呢？
2. 答案是，我们用一个set来存放位数的平方和，假如说一直都到不了1的话，总有一天能刷出set(）有的元素
   到那个时候就return False

"""