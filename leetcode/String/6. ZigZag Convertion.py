class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""

        res = ["" for i in range(numRows)]
        i = 0

        while i < len(s):

            # from up to down
            j = 0
            while i < len(s) and j < numRows:
                res[j] += s[i]
                i += 1
                j += 1

            # from down to up
            j = numRows - 2
            while i < len(s) and j > 0:
                res[j] += s[i]
                i += 1
                j -= 1

        return "".join(res)


"""
https://www.youtube.com/watch?v=8zXTAn7i5rU
这题其实找到规律了就很好写
创建一个多维列表
然后按照列表的
从上往下，再从下往上那样写，最后把每一行给拼起来
"""
