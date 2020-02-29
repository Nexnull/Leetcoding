import collections
class Solution:
    def FirstNotRepeatingChar(self, s):
        s = list(s)
        minIndex = 10000

        collect = collections.Counter(s)
        candidate = []
        for key in collect.keys():
            if collect[key] == 1:
                candidate.append(key)


        for i in candidate:
            minIndex = min(minIndex,s.index(i))

        return minIndex




if __name__ == "__main__":
    solution = Solution()
    solution.FirstNotRepeatingChar("aazbbccd")


"""
这题自己写出来的，感觉做法比较简单粗暴，直接用collections.Counter()把每个元素所出现的
次数找出来，然后把出现次数为1的找出来，然后看哪个最小，比较简单粗暴

看了答案，有种比较优化的方法，就是直接遍历原来的字符串，然后把第一个在candidate里有的找出来
"""