class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0

        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            sum = min(height[left], height[right]) * (right - left)
            if sum > res:
                res = sum
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

"""
https://algocasts.io/episodes/k8GNameQ
答案：// Time: O(n), Space: O(1)
因为是两根柱子围成的面积表示盛水量，且这个面积由最短的那根柱子（木板效应）和宽度决定
所以我们要取一个平衡就是 有两根足够长的柱子，以及相对长的宽度

所以我们从最宽的地方开始遍历，假如说发现两根柱子哪根比较短，我们就移动短的柱子取新的位置
"""