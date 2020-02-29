

class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        res = " "
        lamb = lambda n1,n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        array = sorted(numbers,cmp=lamb)
        return "".join(str(i) for i in array)




if __name__ == "__main__":
    solution = Solution()
    solution.PrintMinNumber()


"""
我的想法：隐约之间感觉有点线索就是

321
32
3

一位位进行对比，比到最小的一位，就放到最前面。感觉有点难写出来
这个思路是错误的

正确思路：
python 2.X sorted 的用法：https://www.runoob.com/python/python-func-sorted.html

sorted(iterable, cmp=None, key=None, reverse=False)

iterable -- 可迭代对象。
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。


  对于有三个数字的情况： [3,32,321] 我们两两进行比较， 332>323 于是，将 3 与 32 交换位置变成 [32,3,321] 而 3321>3213 于是将 3 与 321 继续交换位置到 [32,321,3] ；接着我们继续使用 32 进行比较，由于 32321>32132 将 32与321 进行位置交换为 [321,32,3] 此时，将数组链接起来变成 321323 即为最小的数。
  具体思路：
  （1）先将数字列表转化成字符串链表，这样便于在一个字符串后面直接加上另外一个字符串。也就是 "3"+"321"="3321" 。
  （2）构造一个比较函数，当 𝑠𝑡𝑟1+𝑠𝑡𝑟2>𝑠𝑡𝑟2+𝑠𝑡𝑟1 时我们认为字符串 𝑠𝑡𝑟1>𝑠𝑡𝑟2 。
  （3）将字符串列表按照比较函数的规定进行冒泡排序（或其它方法排序），将定义为”大”的字符串放到最后。而”小”的字符串放在前面。最后将字符串列表链接起来，便是所求。
"""