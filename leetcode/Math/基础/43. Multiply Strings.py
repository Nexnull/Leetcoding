"""
求"123" * "123" = ?
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 and len(num2) == 0: return "0"
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                phigh = i + j; plow = i + j + 1
                sum = res[plow] + product
                res[phigh] += sum // 10
                res[plow] = sum % 10

        final = ""
        for num in res:
            if not (len(final) == 0 and num == 0):
                final += str(num)

        return "0" if len(final) == 0 else final


"""
Time(O(m*n)) Space:O(n)
图解：https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
题解：https://www.youtube.com/watch?v=q3vpdwWR0ag
答案：
这题的写法比较麻烦
1.res的长度应该是 len(nums1) + len(nums2)
然后我们要把两个数组给按照右边对齐
            123
             45
2.然后我们需要从右向左遍历，同时指定两个指针，i,j,一个走上面的数，一个走下面那个数
3.用product来记录num1[i] * num2[j]
45  plow表示5,phigh表示4

**注意，这里的res的index，可能存在多次加减，所以要注意+= 和 = 的关系

4.sum = res[plow]是因为plow这里可能之前存在多个数，导致和>10，然后我们需要考虑进位，
所以sum = res[plow] + product
5.res[phigh] += sum的十位
6.res[plow] = sum的个位

7.最后我们把数组转换为字符串
final的第一个数不能为0，其余的都直接加进去就好了

8.返回结果
"""