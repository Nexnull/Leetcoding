"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Input: "()[]{}"
Output: true

Input: "(]"
Output: false
就是判断左右两边的括号能不能合上
"""


def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if s is None:
        return

    match = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for i in s:
        if i in match.keys():
            stack.append(i)
        else:
            if len(stack) == 0:
                return False

            left = stack.pop(-1)
            if i == match[left]:
                continue
            else:
                return False

    if len(stack) != 0:
        return False

    return True


"""
这题利用stack来做

解法：
从s里拿出一个元素
1.是左括号，则push进stack
2.是右括号，则pop出peak元素
3.s遍历结束时，看看stack是不是空的，如空则完成，没空则false

remark:
1.注意else这种情况，有可能输入的只是一个右字符串，那么pop的话会返回错误结果
所以建议在输入右字符串的时候，先检测一下stack的长度，如果长度为0,那么直接return false
"""