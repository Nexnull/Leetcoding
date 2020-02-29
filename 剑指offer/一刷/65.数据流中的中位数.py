class Solution:
    def __init__(self):
        self.stream = [2,5]

    def Insert(self, num):
        self.stream.append(num)

    def GetMedian(self,enen):
        if self.stream == None:
            return None
        self.stream.sort()
        length = len(self.stream)
        if length % 2 == 1:
            return self.stream[length // 2]
        else:
            return (self.stream[length//2 - 1] + self.stream[length//2])/2.0


if __name__ == "__main__":
    solution = Solution()
    print(solution.GetMedian())




"""
感觉这题就是送分题把，感觉不太可能出这种

看了答案，真的就是弱智题

写了答案更感觉这是个弱智题。。。
牛客网的测试用例写的真是太垃圾了
get median函数里应该加一个无关变量
"""
