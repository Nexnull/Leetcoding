"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example
Given [[0, 30],[5, 10],[15, 20]],
return 2.
给出事件所需要占用的事件，问我们最少需要用多少个会议室。[0，30]需要用一个
[[5,10],[15,20]]需要用一个
原文链接：https://blog.csdn.net/qq508618087/article/details/50762939
"""
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[list[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:x[0])
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
"""
这题的做法是，假如说在同一个时间段，有两个事件需要同时进行，那么就需要两个房间
要是他们的时间是间隔开的，那么只需要同一个房间
事件1：------------------
事件2:          -------------
事件3:                         ----------- 
所以我们只需要两个房间

答案：
https://www.youtube.com/watch?v=wB884_Os58U
time O(nlogn) , space O(n)
我们知道，假如说当前的continer里最早空出来的房间 比 interval开始的时间晚，说明要多开一个房间
1.heap为空，把interval.end加进heap
  heap不为空，且interval.end > continer[0]
  这两种情况，要加入新房间
2.假如说heap不为空 且 interval.end <= continer[0]
  说明不用加新房间，我们只需要更新以下新的结束时间
"""