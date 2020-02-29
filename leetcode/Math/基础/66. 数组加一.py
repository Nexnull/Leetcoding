"""
Given a non-empty array of digits representing a non-negative
 integer, plus one to the integer.
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits or len(digits) == 0: return [1]

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

"""
time:On space O1
https://www.youtube.com/watch?v=6A-DTVB9HT8
答案：
0.遇到这种涉及加法的题，我们需要从后往前遍历
1.[4,1,1,1]正常情况就返回[4,1,1,2]就好
2.例如[4,1,1,9],遍历到9的时候变0，遍历到1的时候+1
3.例如[9,9,9,9],遍历完所有，[0,0,0,0]，然后使得第一位变成1，[0]=1,
然后补上最后一位append(0),[1,0,0,0,0]
"""