class Solution(object):
    def boldWords(self, S, words):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        n = len(S)

        mark = [False] * n

        for i in range(n):
            # 前面检查过的字符串我们就不需要重复检查了
            # 我们只用看当前到最后的字符串能不能和word搭配上
            prefix = S[i:]

            for word in words:
                # 使用这个函数我们不用考虑字符越界的情况
                if prefix.startswith(word):
                    # 这里考虑到index会不会越界
                    # 假如说s能和word对上，那我们把s中对应位置都标志成1
                    for j in range(i, min(i+len(word), n)):
                        mark[j] = True

        ans = ""
        for i in range(n):
            # 确认是以 0001 或者是111这种情况， 是属于加粗字符串的开头，于是我们要加<b>
            if mark[i] and (i == 0 or not mark[i-1]):
                ans += "<b>"
            ans += S[i]
            # 确认是以 1111000 或者是1111这种个情况， 属于加粗字符串的结尾，于是我们要加</b>
            if mark[i] and (i == n-1 or not mark[i+1]):
                ans += "</b>"

        return ans

"""
https://zxi.mytechroad.com/blog/string/leetcode-758-bold-words-in-string/
"""