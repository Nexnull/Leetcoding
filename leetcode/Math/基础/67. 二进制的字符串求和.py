"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = "" ; carry = 0
        for i in range(max(len(a),len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry,val = val//2,val%2
            res += str(val)
        if carry == 1:
            res += str(1)

        return res[::-1]

"""
https://www.youtube.com/watch?v=ZL1zX8Nyk4g
答案：
1.这题不需要写判断corner case,因为假如说a,b = ""那么连for循环都进不了了
2.carry这个变量是记录当前这个index相加是否存在index+1 需要进1
3.for循环我们按照长度长的str来遍历
4.每次for开始，val = carry,就是说把上一位进的1,先传给val
5.val += int(a[-(i+1)]),我们注意是从右向左一位一位加的
6.carry = val//2是因为，假如说要进一的话，那么此时的val = 2 or 3(可能带有上一次的进一)
7.val%2 表示假如val要进1，则清0，不进则保持
8，假如10，10这种情况，进1已经到循环外了，那我们已经让它进
9.加的结果是从左向右加的，所以要[::-1]
"""





