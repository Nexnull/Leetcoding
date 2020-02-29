"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
这个题目说的是，给你两个字符串 s 和 t，你要在 s 中找到一个最短子串，
它包含 t 中所有的字符。如果找不到满足条件的子串，就返回空字符串。
"""
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ""

        # left,right 代表滑动窗口的左右指针
        # start代表最短字串的起点，length代表最长字串的长度
        # requiredCnt 代表我们需要的多少个字母
        # required 是一个hashmap,代表着我们需要的
        left, right = 0, 0
        start, length = 0, len(s) + 1
        requiredCnt = len(t)
        required = Counter(t)

        while right < len(s):
            # 假如说s[right] 是有需求的话(>0),那我们在requiredcnt，
            # 和required 减去它
            if s[right] in required:
                if required[s[right]] > 0: requiredCnt -= 1
                required[s[right]] -= 1

            # 假如说requiredCnt = 0
            # 说明在当前的[left,right] t的全部元素都已经找到了
            # 我们要移动left，去找更短的substring
            while requiredCnt == 0:
                print("hello")
                # 假如当前找到的字串长度小于之前我们找到的,那么更新start 和length
                if right - left + 1 < length:
                    print("start", start, right)
                    start = left
                    length = right - left + 1

                # 然后我们要开始把左指针从当前的left 向右移动
                # 左指针向右移动的时候，同时要把required【left]加回去，因为
                # left 已经不在我们的窗口内了
                # 同时要是required[s[left] > 0，的话，说明我们对s[left】这个
                # 元素是有需求的，所以required 要+1
                # 最后才是左指针向右移动
                if s[left] in required:
                    required[s[left]] += 1
                    if required[s[left]] > 0: requiredCnt += 1
                left += 1

            # 左指针移动完后，就右轮到右指针向右探索了
            right += 1

        return "" if length == len(s) + 1 else s[start:start + length]

"""
https://algocasts.io/episodes/6emEOnpV
 Time: O(n), Space: O(n)
 写法：双指针 + hashmap
答案：
1.algocast用了一个256位的hashmap来创造map,但是我们可以用python 的collection.Counter 来产生一样的效果，就是有些代码需要改一下
2.大体步骤都在上面了
"""









