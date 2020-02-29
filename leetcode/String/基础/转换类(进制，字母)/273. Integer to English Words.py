"""

"""

def __init__(self):
    self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    self.thousands = ["","Thousand","Million","Billion"]

def numberToWords(self, num):
    if num == 0:
        return "Zero"
    res = ""
    for i in range(len(self.thousands)):
        if num % 1000 != 0:
            res = self.helper(num%1000) + self.thousands[i] + " " + res
        num //= 1000
    return res.strip()

def helper(self, num):
    if num == 0:
        return ""
    elif num < 20:
        return self.lessThan20[num] + " "
    elif num < 100:
        return self.tens[num//10] + " " + self.helper(num%10)
    else:
        return self.lessThan20[num//100] + " Hundred " + self.helper(num%100)


"""
https://www.youtube.com/watch?v=qHBEapISpBY
https://leetcode.com/problems/integer-to-english-words/discuss/70688/Python-Clean-Solution
答案：
怎么说把，看看答案是怎么处理的
1.主要分为三个阶段，按逗号来分，Billion _ _, _ _ Million, _ _ thousands, _ _ _
2.然后i 每次++ ，使得res从0 -> 1000 -> 100,000 -> 100,000,000

3. 循环主要处理千位以上的 
   例如：我们之前写切分十进制的时候 是  个位 = num % 10
                              num //= 10

  但我们这里是按照千位来切分，所以一个千位 = num % 1000
                           取余出来的数字，我们把它丢到helper里面进行处理，
                           同时处理完后，我们把 num //= 1000
                           表示取处理下一个一千

4.helper只负责处理小于1000的数字，情况分别有：1.num == 0
                                          2.num < 20 (0-19)
                                          3.num < 100 (20-99)
                                          4. num < 1000 (100-999)

"""