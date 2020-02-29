class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curString = ""
        curNum = 0
        stack = []

        for char in s:
            if char == "[":
                stack.append(curString)
                stack.append(curNum)
                curNum = 0
                curString = ""
            elif char == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif char.isdigit():
                curNum = curNum * 10 + int(char)
            else:
                curString += char

        return curString

"""
https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
答案：
答案比较直接
1.假如说char == "["时，说明我们已经收集到了[前面的数字，以及我们要开始把之前已有的字符串
放进stack,准备与【】内的字符串进行拼接
然后把curNum = 0，用于记录下一个数字
     curString = "" 准备用于记录【】内的字符串

2.char == "]", 说明我们已经应该进行拼接了
  num = []前的数字
  prevString,之前拼好的字符串
  curString = prevString + num*【】括号内的字符串

3. 等于数字的时候，我们要考虑到数字有可能是非个位数
4. char == 字母时，说明此时在【】内，收集括号内的字符串就好了
"""