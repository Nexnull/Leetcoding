class Solution(object):
    def equals(self, sc, pc):
        for i in range(len(sc)):
            if sc[i] != pc[i]:
                return False
        return True

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(s) < len(p):
            return []

        res = []
        sc = [0] * 26
        pc = [0] * 26

        # 先把pc，sc的hashmap给建好，并且先进行第一次比较
        for i in range(len(p)):
            sc[ord(s[i]) - ord("a")] += 1
            pc[ord(p[i]) - ord("a")] += 1

        if self.equals(sc, pc): res.append(0)

        # 然后我们继续比较，我们为了方便把P的长度先弄出来
        # 接下来就是有点滑动窗口的感觉了，在sc的表上操作
        # 把新进入窗口的元素记录在hashmap(i)
        # 把离开窗口的元素记录移除 hashmap[i-pLen]
        pLen = len(p)
        for i in range(pLen, len(s)):
            sc[ord(s[i]) - ord("a")] += 1
            sc[ord(s[i - pLen]) - ord("a")] -= 1
            if self.equals(sc, pc):
                res.append(i - pLen + 1)
        return res

"""
Time: O(n*k), Space: O(k)
https://algocasts.io/episodes/LPmwkomq
答案：
1.建立两个hashmap来代表两个字符串，然后利用滑动窗口来锁定参与对比的元素个数
"""