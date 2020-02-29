"""
Given an array nums, there is a sliding window of size k which is moving
from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums:
            return []

        # window记录的是index, res 记录的是值
        window , res = [] , []
        for i , x in enumerate(nums):
            # 假如index(i) 已经大于滑动窗口的长度了(k)（意味着可以加新元素进窗口了）
            # 且当前窗口的最左边的index(windows[0])，这时上次循环的 < 当前循环，窗口的应当的左边界（i-k)
            # 这时候说明窗口的最左边元素应该被pop掉了
            if i >= k and window[0] <= i - k:
                window.pop(0)

            # 当窗口有值，且窗口的最右边的数<新要加进来的数
            # 就把窗口最右边元素给pop掉
            # 一直重复这个循环
            # 假如新元素比原窗口所有数都大，那就把原窗口给清干净
            while window and nums[window[-1]] <= x:
                window.pop()

            # 理论上，新加入的元素不管大小，在当前回合都不会对他进行任何操作的
            window.append(i)

            # 加入index到了比窗口长度的临界点，说明窗口已经建立起来了
            # 两种情况：原window有比新加进元素大的，那它没被pop掉，返回最左边的（即是窗口里最大的值）
            #         原window没有比新元素大的，说明其他元素被pop掉了，于是返回列表唯一一个元素【0】
            if i >= k-1:
                res.append(nums[window[0]])

        return res


"""
https://www.youtube.com/watch?v=swI1u_gk4MI&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=14&t=633s
这题有两种做法：
1。最大堆，堆的大小为k，那么每次新元素加进堆即可，然后把最上面的数给pop出来
这样的做法是 n * logK因为对heap进行操作的时间复杂度是logk

time O(n) space O(n)
2.使用deque
这题最优解使用deque来做，deque是双端都可以进行插入和删除的队列
    1。窗口剩下的元素都是经过筛选过的（第二步进行筛选），然后我们根据index的推进把窗口左边的元素给清理掉
        1.1或者无论窗口有没有把当前index的数处理掉，都得给新元素让位
    
    2。新加入一个元素前，把原窗口所有小于它的元素都清理掉
    3。然后加入这个元素
    4. 加入index到了比窗口长度的临界点，说明窗口已经建立起来了
       两种情况：原window有比新加进元素大的，那它没被pop掉，返回最左边的（最大的）                                        
       原window没有比新元素大的，说明其他元素被pop掉了，于是返回列表唯一一个元素【0】



"""



