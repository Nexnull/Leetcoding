class Solution:
    def Permutation(self, string):
        if string == "":
            return []
        self.res = []
        self.helper(string,"")

        return sorted(list(set(self.res)))

    def helper(self, string, path):
        if not string:
            self.res.append(path)
        else:
            for i in range(len(string)):
                self.helper(string[:i] + string[i+1:] , path + string[i])



if __name__ == "__main__":
    solution = Solution()
    solution.Permutation("abc")

"""
https://www.youtube.com/watch?v=oCGMwvKUQ_I
leetcode上有一系列题，属于backtrack类：子集,排列,组合（subset,Permutation，combination)
leetcode46

思路：
其实原理简单暴力，就是先确定第一位，然后再确定第二位，最后再确定第三位
然后用递归的方法把所有结果给弄出来，因为是把每种可能都写出来了
所以最后在return那里去除重复项

关键地方在于，理解helper里面的处理项，其实切片意在表示，定一，移二的思想
string[:i] + string[i+1:] 表示除了被定元素以外别的字符串
res 结果list,有存在重复项 
path + string[i] 前面定下的元素+这次循环定下的元素
"""