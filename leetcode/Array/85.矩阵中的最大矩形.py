class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0 or not matrix[0] or len(matrix[0]) == 0:
            return 0
        heights = [0] * len(matrix[0])
        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0

            res = max(res, self.largestRectangleAreaStack(heights))
        return res

    def largestRectangleAreaStack(self, heights):
        if not heights or len(heights) == 0:
            return 0
        res = 0
        n = len(heights)
        stack = []
        r = 0

        for r in range(n + 1):
            h = 0 if r == n else heights[r]

            while len(stack) != 0 and h < heights[stack[-1]]:
                index = stack.pop()
                l = -1 if len(stack) == 0 else stack[-1]
                res = max(res, heights[index] * (r - l - 1))

            stack.append(r)
        return res

"""
https://algocasts.io/episodes/6emEjnGV
Time: O(n*m) space:O(n)
答案：
这里的辅助函数，我们复用了第84题的函数

所以在主函数里面，我们只需要构造一个跟84有相同结构的长度数组，然后把它丢进辅助函数李敏啊
就能得出正确答案了
"""