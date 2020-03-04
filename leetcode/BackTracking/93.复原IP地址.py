# coding=utf-8
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.s = s
        self.res = []

        self.helper(0, 4, "")
        return self.res

    def helper(self, index, remain, cur):
        if remain == 0:
            if len(self.s) == index:
                self.res.append(cur[:])
            return

            # 因为我们是用切片的做法，[index,index+i),等于能取到012这三位数字
        for i in range(1, 4):
            if index + i > len(self.s):
                break

            # 因为 i = 1的时候， 只能取到 [index]这一位
            if i != 1 and self.s[index] == "0":
                break

            temp = self.s[index:index + i]
            # 会出现555这种情况，要跳过，我们只要0-255
            val = int(temp)
            if val <= 255:
                # 当remain 等于1的时候，然后下一次递归remain=0，说明已经遍历完了，所以不应该加.
                self.helper(index + i, remain - 1, cur + temp + ("" if remain == 1 else "."))


"""
https://www.youtube.com/watch?v=b8_w2ljAzeU
看这个解释就可以了
"""

