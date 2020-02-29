""""
看到这一题第一个想法就是把字符串切片
然后从右边拼上去
...
然后就过了
"""

class Solution:
    def LeftRotateString(self, s, n):
        leftpart = s[:n]
        res = s[n:] + leftpart
        return res