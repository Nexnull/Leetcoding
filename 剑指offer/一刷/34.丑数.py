
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        baselist = [1]
        min2 = min3 = min5 = 0

        while len(baselist) <= index:
            temp = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)
            baselist.append(temp)

            # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
            while baselist[min2] * 2 <= temp:
                min2 += 1

            # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
            while baselist[min3] * 3 <= temp:
                min3 += 1

            # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
            while baselist[min5] * 5 <= temp:
                min5 += 1

        return baselist[index - 1]


if __name__ == "__main__":
    solution = Solution()



"""
刚看了lambda 与filter函数，可以用来做这一题
实际上不可以

正确思路：
丑数只能是2，3，5的倍数。所以我们得一路找出所有的丑数，如何找丑数，就是用2，3，5各自丑数
数列的最小值，然后再min( x*2,x*3,x*5)

https://blog.csdn.net/qq_20141867/article/details/81060581

"""