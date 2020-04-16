class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # cut[i] 表示 从[0 - i-1]上，有多少个回文子串
        # 因为我们有len(s)个元素， 所以假如说要表示[0 - len(s)]的话，我们需要长度为len(s)+1个长度
        # 我们在这里设定最大预设值，那么就是每个元素的间隙都能切，形成回文字串
        # 例如2，可以切一次，  3，可以切两次
        # 所以这里是i-1
        cut = [i - 1 for i in range(len(s) + 1)]

        for p in range(len(s)):
            self.expend(s, p, p, cut)
            self.expend(s, p, p + 1, cut)

        return cut[len(s)]

    def expend(self, s, i, j, cut):

        # 假如说 [i - j] 都是回文字串，那么我们可以理解为 cut[j+1] = cut[i] + 1
        # 因为 cut[i] 表示了从[0 - i-1] 有多少个回文字串， 而 [i - j]又是另一个回文字串
        # 所以 cut[j+1] = cut[i] + 1
        # 又因为我们的 cur[j+1] 有个最大的预设值，所以我们要取两者中比较小的哪一个
        while i >= 0 and j < len(s) and s[i] == s[j]:
            cut[j + 1] = min(cut[i] + 1, cut[j + 1])
            i -= 1
            j += 1

"""
Time: O(n^2), Space: O(n)
https://algocasts.io/episodes/k8GN2lGe

"""