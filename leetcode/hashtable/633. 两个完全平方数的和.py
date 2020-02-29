"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
"""

class Solution(object):
    def isSquare(self, num):
        x = int(num**0.5)
        return x*x == num

    # Time: O(c ^ 1 / 2), Space: O(1)
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c**0.5) + 1):
            rest = c - i**2
            if self.isSquare(rest): return True
        return False

    # Time: O(c ^ 1 / 2), Space: O(c ^ 1 / 2)
    def judgeSquareSumHashmap(self, c):
        hashset = set()
        for i in range(int(c**0.5) + 1):
            hashset.add(i**2)
            rest = c - i**2
            if rest in hashset:return True
        return False

    # Time: O(c ^ 1 / 2), Space: O(1)
    def judgeSquareSumTwoPointers(self, c):
        left = 0
        right = int(c**0.5)+1

        while left <= right:
            sum = left**2 + right**2
            if sum == c: return True
            elif sum > c: right -= 1
            else: left += 1
        return False

"""
https://algocasts.io/episodes/ezpl3PGE
这题有多种解法，可以给我们多种启发
答案：
1.暴力破解
2.set(),two sum的做法

"""

