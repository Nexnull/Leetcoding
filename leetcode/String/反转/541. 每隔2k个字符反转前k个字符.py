class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return

        s = list(s)
        for start in range(0, len(s), 2 * k):

            i = start
            # 假如 abcd , k = 2, 这就意味着我们只翻转ab
            # 所以start = start + k - 1
            # 在这里我们要对start + K -1 可能的越界情况做处理
            j = min(start + k - 1, len(s) - 1)
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)


"""
时间复杂度：O(N)O(N)，其中 NN 是 s 的大小。我们建立一个辅助数组，用来翻转 s 的一半字符。
空间复杂度：O(N)O(N)，a 的大小。
https://leetcode-cn.com/problems/reverse-string-ii/solution/fan-zhuan-zi-fu-chuan-ii-by-leetcode/
"""