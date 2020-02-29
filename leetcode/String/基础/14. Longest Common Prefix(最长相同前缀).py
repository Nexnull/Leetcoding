"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0: return ""

        shortest_str = min(strs, key=len)

        for i in range(len(shortest_str)):
            for string in strs:
                if shortest_str[i] != string[i]:
                    return shortest_str[:i]

        return shortest_str

"""
Time:O(N^2) space:O(1)
答案
1.首先我们先把字符串列表里长度最小的子串(shortest_str)给找出来
2.然后遍历这个这个字串,并横向对比所有字串，假如说shortest_str[i] != string[i]
  那么就返回最后从开头到第i位的切片
3.正常情况下都是可以返回出结果的，除非: 1.["abc"] [""]
                                这种情况就会跳过shortest_str[i] != string[i]的逻辑，无法return
                                    2.["ab","ab"]
                                完全相同的子串，那么也会跳过不想等的逻辑
 所以这里最好的解决办法就是return shortest_str.
"""

