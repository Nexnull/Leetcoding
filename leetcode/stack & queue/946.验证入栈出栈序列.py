"""
Given two sequences pushed and popped with distinct values, return true if and only if this
could have been the result of a sequence of push and pop operations on an initially empty stack.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) != len(popped):
            return False

        stack = []
        p = 0
        for num in pushed:
            stack.append(num)
            while len(stack) != 0 and stack[-1] == popped[p]:
                stack.pop()
                p += 1

        return len(stack) == 0

"""
Time: O(n), Space: O(n)
https://algocasts.io/episodes/KApAz4W6
答案：
1.我们先把pushed的元素一个个的都pushed 到stack里面去（因为我们要模拟最真实的出入栈序列）
2.定义一个指针p = 0, 用来按顺序获取popped 元素
3.当栈顶元素 == popped的第一个元素时，stack.pop, p移向下一个element
4.假如这样执行完了，stack = [] , 说明pushed 和 popped确实是出入栈顺序是一致的

"""