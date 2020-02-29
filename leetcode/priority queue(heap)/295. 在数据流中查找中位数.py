"""

"""
from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
    #  Time: O(log(n))
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small,-num))
        else:
            heappush(self.small, -heappushpop(self.large,num))

    # O（1）
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0])/2.0
        else:
            return float(self.large[0])

"""
https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
https://algocasts.io/episodes/VlWdOvp0
答案：
1.这题我们运用了一个最大堆(self.small)和一个最小堆(self.large)
2.由于我们要找中位数，所以我们让两个堆的数量保持在一个相同 或 large比small多一个数
  总共有2n+1个数，small里有n个数，large里面有n+1个，那么我们返回large里面最小的那个数就好了
  总共有2n个数，  small里有n个数，large里面有n个数，那我们返回 samll里最大的，large里面最小的，/2.0就好了

3.一个数进来
  如果len相同：那我们要往large里加一个数，所以我们得把那个数先丢进samll里面，验证一波,然后把pop出来的数字，放入large中
  why?
  因为假如说num 是small里最大的，那么它也会被pop出来，如果它并不是samll里最大的，那么就把small里最大的pop出来
  
  如果len不同（len(large)> len(small)):我们要往small里加数，我们得先把num 丢进large里验证一波，然后pop出，放入small中
  
注意：
1.我们用 -num 来构造最大堆，给small使用
2.所以最后计算和的时候， large[0] - small[0]
"""