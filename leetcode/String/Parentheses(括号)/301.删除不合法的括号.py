"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.remove(s, result, 0, 0, ('(', ')'))
        return result


        def remove(self, s, result, last_i, last_j, par):
            count = 0
            for i in xrange(last_i, len(s)):
                if s[i] == par[0]: count += 1
                if s[i] == par[1]: count -= 1
                if count >= 0:
                    continue

                #当count<0,说明出错了，进行删除，从上一次被删除的元素出发，到i+1
                for j in xrange(last_j, i + 1):
                    if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                        self.remove(s[:j] + s[j + 1:], result, i, j, par)
                return

            # 正向删除之后，有可能是左括号数量多与右括号，所以我们需要反转一遍，再检查
            # 一次
            reversed_s = s[::-1]
            if par[0] == '(':
                self.remove(reversed_s, result, 0, 0, (')', '('))
            else:
                result.append(reversed_s)

"""
思路来源：https://www.youtube.com/watch?v=llYfOsGSvdc
"""