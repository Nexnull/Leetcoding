"""
"()(())"
output: 6

Input: ")()())"
Output: 4
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0: return 0
        n = len(s)
        maxLen = 0

        stack = [-1]
        for i in range(len(s)):
            if stack[-1] != -1 and s[stack[-1]] == "(" and s[i] == ")":
                stack.pop()
                maxLen = max(maxLen , i - stack[-1])
            else:
                stack.append(i)
        return maxLen

"""
// Time: O(n), Space: O(n)
https://algocasts.io/episodes/n5GqbVpA
答案：
1.algocasts 里的p,代表的就是stack peek元素
2.
"""