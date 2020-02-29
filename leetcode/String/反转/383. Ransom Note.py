"""
Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
假如说前面的字符串能由后面的字符串构成（不需要连续），则放回True
"""

class Solution(object):
    def canConstruct(self, short, long):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not short or (not short and not long):return True

        hashmap = [0]*26

        for char in long:
            index = ord(char) - ord("a")
            hashmap[index] += 1

        for char in short:
            index = ord(char) - ord("a")
            hashmap[index] -= 1
            if hashmap[index] < 0:return False
        return True

"""
https://leetcode.com/problems/ransom-note/discuss/85783/Java-O(n)-Solution-Easy-to-understand
Time:O(n) space:O(n)
答案：
操作和387题有点像，但是难度降低了很多
总体上上还是运用了一个26字母的hashmap，来计算字符串出现的次数
1.创建长度为26的hashmap,用来存放每个字母在long 中出现的次数
2.我们一遍遍历short,一遍减short里出现过的字母
3.当出现short[index] < 0的时候,说明这个字母在long里面出现的次数并不够，所以return False
4.若没出现问题，return True
"""