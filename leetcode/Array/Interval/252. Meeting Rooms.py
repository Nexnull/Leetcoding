"""
给出开会时间，问一个人能不能同时参加所有会议（就是会议之间不能有交集）
Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""
class Solution(object):
    def meetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: Boolean
        """
        intervals.sort(key=lambda x: x[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][-1]:
                return False
        return True

"""
Time:O(nlogn), Space:O(1)
答案：
1.排序
2.检查是否有 后.start < 前.end
  有的话则说明这个人去不了，因为前一个开会时间太长了，他赶不上不后面的
"""
