"""
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
class Solution(object):
    def expend(self,string,left,right):
        count = 0
        while left <= right and left >= 0 and right < len(string) and\
                string[left] == string[right]:
            left -= 1
            right += 1
            count += 1

        return count
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s is None:return 0
        res = 0
        for i in range(len(s)):
            res += self.expend(s,i,i)
            res += self.expend(s,i,i+1)
        return res




"""
https://algocasts.io/episodes/dbGY2p5V
// Time: O(n^2), Space: O(1)
答案：
aba
1.当我们遍历到a的时候，他自己算一个回文字串
2.然后我们向外扩展
3.到b的时候，b为一个回文字串，向外扩展,a == a,所以aba算一个回文子串
4.考虑情况 abba，所以我们要res += self.expend(s,i,i+1)
"""