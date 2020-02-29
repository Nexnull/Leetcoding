

class Solution:
    def StrToInt1(self, s):
        bit = 1
        res = 0

        if len(s) == 0:
            return 0
        if len(s) == 1 and  not s[0].isdigit():
            return 0

        for i in range(len(s) -1 , -1, -1):
            if s[i].isdigit():
                res += (ord(s[i]) - ord("0"))*bit
                bit *= 10
                continue
            else:
                if i == 0 and (s[i] is "+" or s[i] is "-"):
                    continue
                else:
                    return 0
        print(-1*res  if s[0] is "-" else res)
        return -1*res  if s[0] is "-" else res




if __name__ == "__main__":
    solution = Solution()
    solution.StrToInt1(" ")




"""
下载了答案以后然后来看这道题
就是很简单的一个把字符串变成整数的题。
然后有一些判断条件
1、空串检验，2、数字合法性检验，3、正负数数字区分，4、只有一个正负号时

同时间不能应用任何函数进行类型转换，所以只能使用ascii码来进行转换
python ord() 能把一个数转成ascii码


"""
