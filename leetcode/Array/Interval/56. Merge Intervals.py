"""
融合interval
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
注意，这题的intervals给的是没有排序过的
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals) == 0: return []

        intervals.sort(key = lambda x: x[0])
        merge = []
        for interval in intervals:
            #    []  or  [1,3] [4,5]
            if not merge or merge[-1][-1] < interval[0]:
                merge.append(interval)
            # [1,3] [2,4]
            else:
                merge[-1][-1] = max(merge[-1][-1],interval[-1])
        return merge

"""
https://leetcode.com/problems/merge-intervals/solution/
Time complexity : O(nlogn)
Space complexity : O(1) (or O(n))
答案：
此题思路不难
1.首先我们得先把intervals按照第一个元素的大小排序好（从小到大）
2.然后我们遍历intervals，里面有三种情况
2.1 第一种是merge[[1,3]],interval[4,5] 
    那么interval最小元素已经大于merge的最右边了，所以不能融合，只能添加
2.2 第二种是merge[],所以无论第一个interval是啥，直接append
2.3 第三种是merge[[1,3]],interval[2,4]
    这时候我们看出来了merge最右边大于interval的最左边，所以可以融合
    这时我们要确定融合后的右边界，就是max(merge:3,interval:4)
"""