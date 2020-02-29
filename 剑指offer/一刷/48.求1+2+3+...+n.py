
class Solution:
    def Sum_Solution(self, n):
        # write code here
        res = n
        temp = n > 0 and self.Sum_Solution(n-1)
        res += temp
        return res


if __name__ == "__main__":
    solution = Solution()
    solution.Sum_Solution(4)





"""

没有什么想法，学习下把

答案：
利用逻辑与的短路特性实现递归终止。
其中： 
     “or”运算符表示“或”，有一个为真则全部为真；前半部分判断出来是真的，后半部分就不再进行运算了。
     “and”运算符表示“与”，前一项为假则整个表达式为假，因此可以利用这个性质进行递归运算或者达到整洁代码的目的。
     
     
     temp = n > 0 and self.Sum_Solution(n-1)
     当n == 0的时候，就不会继续递归下去了，temp会等于false,因为前面有false,and不会
     再执行后半段了
"""