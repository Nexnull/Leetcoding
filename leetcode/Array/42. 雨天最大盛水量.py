class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 0: return 0

        left_max = -1
        right_max = -1
        res = 0
        record = [0 for i in range(len(height))]

        for i in range(len(height)):
            left_max = max(height[i],left_max)
            record[i] = left_max

        for i in range(len(height)-1,-1,-1):
            right_max = max(height[i],right_max)
            record[i] = min(right_max,record[i])
            res += (record[i] - height[i])

        return res

"""
https://algocasts.io/episodes/eAGQ1MG4
这题其实不难，看algocast的第一种解法
主要是，我们要从左到右遍历一次，记录当前到当前位置为止，从左到当当前位置的最大值（意味着左墙壁）
再从右向左遍历一次，记录到当前位置为止，从右往左的最大值（意味着右墙壁）
最后我们记录当前位置左右墙壁的最小值（木桶效应）
然后用当前左右墙壁的最小值 - 当前位置的高度，得到当前index的盛水亮
然后我们把所有index的盛水量都加在一起得到最后的结果
"""