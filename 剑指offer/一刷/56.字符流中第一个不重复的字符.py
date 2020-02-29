
class Solution:
    def __init__(self):
        self.stream = {}
        self.str = ""

    # 返回对应char
    def FirstAppearingOnce(self):
        for i in self.str:
            if self.stream[i] == 1:
                return i
        return "#"


    def Insert(self, char):
        if char not in self.stream.keys():
            self.stream[char] = 1
        else:
            self.stream[char] += 1
        self.str += char



"""

额，这题的答案秀的我头麻，原来insert函数是要用来加字符来让我们判断的
然后firstappear()是为了能随时找到之前insert的字符，只出现过一次的选项

但是有个问题，字典是无序的，要怎么找出第一个加进去的呢？

答案：
对于上面的问题，我们需要用一个string来计算字符串的顺序

"""