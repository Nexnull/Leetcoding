"""
反转字符串
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 0:
            return s

        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

"""
双指针，交换前后两个指针
// Time: O(n), Space: O(1)
1. 注意 i < j时循环才能进行， 因为i = j时，list[i] = list[j]交换无意义
                               i > j时，会把之前交换过的再交换回来
"""