class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for char in num:

            while k and stack and int(char) < int(stack[-1]):
                stack.pop()
                k -= 1

            stack.append(char)

        while k:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        # 解决 "0200"的情况，因为要输出"200"
        return str(int("".join(stack)))

"""
https://blog.csdn.net/fuxuemingzhu/article/details/81034522
答案：
1.我们这次是从头到尾遍历，
"""