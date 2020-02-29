import collections

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        tinput = sorted(tinput)
        return tinput[:k]

if __name__ == "__main__":
    solution = Solution()






"""
想到比较简单粗暴的方法就是先排序一遍，然后直接输出一个切片

"""