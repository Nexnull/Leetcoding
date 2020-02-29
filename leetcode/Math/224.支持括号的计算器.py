class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0: return 0

        res, sign, num, stack = 0, 1, 0, []
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char in ["-", "+"]:
                res += sign * num
                sign = [-1, 1][char == "+"]
                num = 0

            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif char == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0

        return res + sign * num

"""
https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
答案：
首先先完成不带括号的计算过程
0.sign 表明了num的是正还是负，它的顺序应该是 sign在num 之前， 例如 -12 , +5
1.假如char是数字，我们有可能遇到"12"这种多位的数字，所以我们要 num = num * 10 + int(char)处理
2.假如char是符号，那么我们先把前面的 -12,+5给加进res, 然后这时候才确定当前的sign是什么
  如果char == "1", 那么[-1,1][1] = 1
  然后由于上一个num已经处理完了，所以我们要把num给清零

其次完成带括号的计算过程
1.先说")", 我们先把括号内的最后一次计算给完成了，res += sign+num，
  然后计算结果已经加到了res里面，所以res代表括号内的结果
  例如： 1 + (4+9) ,  此时[1,+] 仍热在stack里面
  但现在等式变成了 1 + res(13)
  又因为stack里面的符号，代表的是括号数的符号
  所以我们要先 res*= stack.pop() 
  然后再加上1
  最后我们再将num给清零
  
2."("
   因为我们要先计算括号内的元素，所以我们暂时先将括号外的元素和符号储存在stack里，先放res,再放sign
   这个sign是括号和的符号，所以要晚放一步
   
   最后因为我们要进入括号内，所以我们先默认括号内的第一个数是正数，因为即使第一个数是-5,那也会进入符号判断
   所以sign在这里我们可以直接把它设成1
   括号外的res已经被放入stack了，现在的res是要记录括号内的和，所以res=0

最后：
1.我们遇到数字时更新num,遇到符号或")"是更新res
2.由于我们只在遇到符号或者")"才更新res, 假如说1+1，最后一个字符是非符号
  所以我们要在最外面的时候， 再更新一次res



"""