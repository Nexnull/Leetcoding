"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""

        while n > 0:
            if n % 26 == 0:
                res += "Z"
                n -= 26
            else:
                res += chr(n % 26 - 1 + ord("A"))
                n -= n % 26
            n //= 26

        return res[::-1]

"""
https://www.cnblogs.com/grandyang/p/4227618.html
答案：
两种情况
1.当n%26 == 0时，说明这个时候加的数应该是Z，
但是0 和 ord("A") 无法反应加出来为26，所以我们这里直接加Z
同时减去26（说明最后一位已经处理完了）

2.当n%26 != 0时,说明这个时候加的数应该是A-Y
因为（1-25）% 26,都是非0的，所以他们都可以恰如其分得表达A-Y
为啥要-1呢： 因为 1对应A
            假如说 n = 1 , n % 26 = 1 , char(1 + ord("A")) = "B"
            所以我们要减去一个1
            然后 n- (n%26) （说明最后一位已经处理完了）
3. n//26,准备处理下一位
4. 因为我们是从后往前处理，但是构成数字母的时候是从前往后构成，所以要[::-1]            
"""