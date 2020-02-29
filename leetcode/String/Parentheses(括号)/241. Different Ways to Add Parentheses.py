class Solution(object):
    def diffWaysToCompute(self, inputs):
        """
        :type input: str
        :rtype: List[int]
        """
        if inputs.isdigit():
            return [int(inputs)]
        res = []

        for i in range(len(inputs)):
            if inputs[i] in "+-*":
                part1 = self.diffWaysToCompute(inputs[:i])
                part2 = self.diffWaysToCompute(inputs[i + 1:])
                for x in part1:
                    for y in part2:
                        res.append(self.helper(int(x), int(y), inputs[i]))
        return res

    def helper(self, x, y, op):
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y

"""
https://www.youtube.com/watch?v=gxYV8eZY0eQ，看思路
https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-solution-(divide-and-conquer). 看解法

答案：
这题利用了，divide and conquer
1.我们把每一个符号，都看作是一个分割点，每次把左右两边的给计算出来（part1,part2）
2.然后part1,part2继续分割，直到无法分割为止，然后part1,part2会返回一个记录着不同值的res
3.然后我们进行最后的合并，就是把它放到两个part的res的每个数，根据他们的符号，来放进helper里
  从此计算出他们不同的值



"""