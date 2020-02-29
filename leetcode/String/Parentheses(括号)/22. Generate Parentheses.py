"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
n为括号数量，要求要形成有效括号才能返回结果
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n is None:
            return []
        self.res = []
        self.helper(0,0,n,"")
        return self.res

    def helper(self,left,right,n,string):
        if left == n and right == n:
            self.res.append(string)
            return
        if left < n:
            self.helper(left + 1, right , n , string + "(")
        if right < n and right < left:
            self.helper(left , right + 1, n , string + ")")


"""
https://www.youtube.com/watch?v=xtDjDTFk-Cw&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=31
时间复杂度：O(2^n)
假如说n = 3,那就意味着我们需要6个空位来填，要是无脑递归的话，那么就会有2^6个结果
于是我们可以剪枝来优化这种情况

1.left,right是用来计算左括号和右括号数量的变量
2.我们得确立一个观念，就是（）是一个括号，）（不是一个括号，所以我们放左括号的优先级
永远是大于右括号，所以我们第二个if 语句用来放左括号。我们不乱放右括号，从一定角度
来说，其实已经是剪枝了（去掉不可能的答案）
3.三是等于在2的基础上进行递归了，然后有个条件得注意
就是    right < left .因为假如说右括号数量比左括号多，这个字符串就肯定是废了

"""

