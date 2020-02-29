class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        do = 0
        be_do = 0
        for token in tokens:
            if token not in ["+","-","*","/"]:
                stack.append(int(token))
            else:
                do = stack.pop()
                be_do = stack.pop()
                if token == "+":
                    stack.append(be_do + do)

                elif token == "*":
                    stack.append(be_do * do)

                elif token == "/":
                    stack.append(int(float(be_do) / do))

                elif token == "-":
                    stack.append(be_do - do)

                else:
                    stack.append(int(token))

        return stack.pop()


"""
https://www.youtube.com/watch?v=eBkHqGMVeiY&t=328s
https://leetcode.com/problems/evaluate-reverse-polish-notation/
思路比较简单粗暴吧
他这里的计算分风格是 只要你是  be_do do 符号， 不管是什么符号，优先级都是一样的，都是 be_do 符号 do
所以我们存进stack里是 [be_do, do], pop(）的顺序是， do, be_do
然后进行操作就好了

注意，在python里面 遇到 -1/22 这种情况，还是会= -0.004xxxx
    但是这里要求的是 -1/22 = 0, 所以我们用 int(float(be_do) / do 来使-0.0004x变成0
"""