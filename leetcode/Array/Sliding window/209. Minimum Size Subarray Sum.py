"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray(连续的子array) of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""
from sys import maxsize
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = maxsize
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while left <= i and sum >= s:
                res = min(res, i - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if res == maxsize else res

"""
Time O(n) , space O(1)
答案：
1.这题用滑动窗口解（又可以说是two pointers）
2.关键是建造一个区间，使这区间时刻保持在一种稳定的状态（在s上下徘徊）
3.每次循环都给sum +新元素
4.假如区间sum >= s , 则往区间最前面的元素給删除
然后时刻 求当前情况的区间最小元素个数，当遍历完成后，也实现了解答

注意：
1.为什么sum一定要 >= 呢?
2.为什么while循环里面，res = min()不能放在最后一行？


"""