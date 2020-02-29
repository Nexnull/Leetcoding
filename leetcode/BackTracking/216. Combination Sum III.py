"""
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and
each combination should be a unique set of numbers.
Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
"""
class Solution(object):
    def combinationSum3(self, length, target):
        """
        :type length: int
        :type target: int
        :rtype: List[List[int]]
        """
        if length < 1: return []
        self.res = []
        self.helper([],0,length,target)
        return self.res

    def helper(self, temp, cur, length , target):
        if len(temp) == length and target == 0:
            self.res.append(temp[:])
            return

        for i in range(cur, 10):
            temp.append(i)
            self.helper(temp, i + 1, length,target - i)
            temp.pop(-1)

"""
自己写出来的。。。

"""
