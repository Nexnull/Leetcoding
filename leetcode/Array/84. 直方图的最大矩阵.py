class Solution(object):
    # O(n^2) O(1)
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights or len(heights) == 0: return 0
        res = 0
        n = len(heights)
        
        for i in range(n):
            height = heights[i]
            left = i
            right = i
            while left >= 0 and heights[left] >= height: left -= 1
            while right < n and heights[right] >= height: right += 1
            res = max(res, height*(right - left - 1))
        
        return res

    # O(n) O(n)
    def largestRectangleAreaStack(self, heights):
        if not heights or len(heights) ==  0:
            return 0
        res = 0
        n = len(heights)
        stack = []
        r = 0

        for r in range(n+1):
            h = 0 if r == n else heights[r]

            while len(stack) != 0 and h < heights[stack[-1]]:
                index = stack.pop()
                l = -1 if len(stack) == 0 else stack[-1]
                res = max(res, heights[index] * (r - l - 1))

            stack.append(r)
        return res


"""
https://algocasts.io/episodes/RVmVlopQ
答案：
1.第一种做法比较简单直接，它的做法是，遍历整个数组(python不能过，java能过)
    然后拿到数组中的每一个高度后，创建两个指针，向两边扩展，遇到比自己大的数，就继续扩展，遇到比自己小的数，就停止扩展。
    这是因为我们把当前遍历到的高度，作为我们一个大矩形的高度，所以只有当左右直方图都比自己高的时候，才能继续走下去
    
2.第二种做法有点抽象，我到现在也只稍微理解了点
  同样的，我们也是遍历整个高度数组，同时把 i对应的数h 作为高度
  
  当 h >= 栈顶元素时，我们一直把h给加入stack中
  当 h < 栈顶元素时，我们开始进行操作
  例如 [1,2,3,4] h = 3
  这时候我们可以看到，h < 4, 这时候我们就要开始评估矩形的宽度了，因为以3为高度的话，至少栈顶元素，是可以被加进宽度里的
  这里要记住，我们需要的矩形，每跟柱子高度都至少要 >= h. 
  所以现在得出的矩形， 和第一问我们找出来的矩形，其实是一样的，但是这个因为只需要遍历一遍，所以速度上大大提升了
"""


