
class Solution:
    def replaceSpace(self, s):

        if s == None:
            return

        string_amount = len(s)
        space_amount = 0
        for i in s:
            if i == " ":
                space_amount += 1

        new_length = string_amount+space_amount*2
        index_origin = len(s) - 1
        index_new = new_length - 1
        new_string = [None]*(string_amount+space_amount*2)

        while index_origin >= 0 and index_new >= index_origin:
            if s[index_origin] == " ":
                new_string[index_new] = "0"
                index_new -= 1
                new_string[index_new] = "2"
                index_new -= 1
                new_string[index_new] = "%"
                index_new -= 1
            else:
                new_string[index_new] = s[index_origin]
                index_new -= 1
            index_origin -= 1

        print(new_string)
        print("".join(new_string))


if __name__ == "__main__":
    solution = Solution()
    print(solution.replaceSpace("hello world"))






"""
虽然python有函数可以直接做，但是还是本着学习的原则
看看需要用到什么算法

答案：

在当前字符串替换，怎么替换才更有效率（现有的replace方法）。
从前往后替换，后面的字符要不断往后移动，要多次移动，所以效率低下
从后往前，先计算需要多少空间，然后从后往前移动，则每个字符只为移动一次，这样效率更高一点。

首先我们得构建出一个足够放替换后字符串长度的列表
然后从后往前一个个填这个空列表的元素
遇到正常的，我们就直接填正常的
遇到空格，我们就把%20 一个个往上填
最后join一下

"""