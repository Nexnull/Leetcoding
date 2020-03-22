class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)

        # 我们要使第一个字符串保持小于等于第二个字符串,这样方便下面统一处理
        # 假如说不满足的话,我们就让他们换个位
        if ls > lt:
            return self.isOneEditDistance(t, s)

        # 假如说长度差大于二的话,那编辑距离不可能为1
        if lt - ls >= 2:
            return False

        # 我们以长度短的为指针
        for i in range(ls):
            if s[i] != t[i]:

                # 假设长度相等
                if lt == ls:
                    return s[i + 1:] == t[i + 1:]
                # 长度不等,且t长点,且当前index上的数不同
                else:
                    return s[i:] == t[i + 1:]

        return ls + 1 == lt

"""
https://leetcode-cn.com/problems/one-edit-distance/solution/xiang-ge-wei-1-de-bian-ji-ju-chi-by-leetcode/
"""