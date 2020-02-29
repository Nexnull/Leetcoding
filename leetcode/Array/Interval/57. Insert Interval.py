"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
注意：这题题目给的intervals是排序好的
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res , new = [] , newInterval

        for index,interval in enumerate(intervals):
            if interval[-1] < new[0]:
                res.append(interval)
            elif interval[0] > new[-1]:
                res.append(new)
                return res + intervals[index:]
            else:
                new[0] = min(new[0],interval[0])
                new[1] = max(new[1],interval[1])
        res.append(new)
        return res
5
"""
https://www.youtube.com/watch?v=WBYCD9qluVg
答案：
看这题你怎么理解了，也可以使用56题的解法，先把newinterval加进interval
然后剩下的操作与56题一摸一样。但是时间复杂度为 Onlogn,空间复杂度O(1)

# O(n) time and space
同样是三种情况
1.假如说interval[1,3] new[4,5](interval.end < new.start),那么append(interval)
2.假如说interval[11,15] new[2,8](interval.start > new.end),那么append(new)
3.假如说上面两个情况都不是，new的start,end是在两个不同的interval里面的
  那么会有融合的情况，所以我们要把new的start = min(interval.start,new.start)
                              new的end = max(interval.end, new.end)
  做完之后我们什么都不用操作，继续循环，一直等到第二步，出现一个interval不在这个范围内，那么append(n)
4.假如说new是最大的，那么循环结束后我们需要把append(new)

"""

