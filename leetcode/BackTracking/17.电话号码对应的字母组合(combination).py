class Solution(object):
    def __init__(self):
        self.mapping = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if "1" in digits or "0" in digits or len(digits) == 0 or digits is None:
            return []
        self.res = []
        self.helper(digits, 0, "")
        return self.res

    def helper(self, digits, index, ans):
        if len(ans) == len(digits):
            self.res.append(ans[:])
            return
        chars = self.mapping[ord(digits[index]) - ord("2")]

        for char in chars:
            self.helper(digits, index+1, temp+char)


"""
答案：
其实这题就等于39题，combination Sum
只不过他跟我们绕了一下弯子，给了点数字，让你去转换

思想还是，假如说有digits 是 234， 然后234，各自对应着三个字符
我们一次确定一个index，例如先确定2，2下面有3个字符，所以我们用for循环去遍历完这三个字符
然后我们把确定下来的index=2,和结果，放入下一个helper
重复这种循环
"""