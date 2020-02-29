class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0: return 0

        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = mapping[s[len(s)-1]]
        for i in range(len(s)-2,-1,-1):
            if mapping[s[i]] < mapping[s[i + 1]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]
        return res

"""
Time: O(n), Space: O(1)
答案：
小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；
小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数
"""