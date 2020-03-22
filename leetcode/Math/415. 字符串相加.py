class Solution(object):
    def addStrings(self, nums1, nums2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p1 = len(nums1) - 1
        p2 = len(nums2) - 1

        res = ""
        next = 0
        while p1 >= 0 or p2 >= 0 or next != 0:
            num1 = int(nums1[p1]) if p1 >= 0 else 0
            num2 = int(nums2[p2]) if p2 >= 0 else 0
            sum = num1 + num2 + next

            next = sum // 10
            sum %= 10

            # 这里要注意一个顺序的问题
            res = str(sum) + res
            p1 -= 1
            p2 -= 1

        return res

"""
这题算是一种小升华
其实里面很多东西都已经是考虑过后我们进行精简的
1. sum >= 10的情况，  sum // 10 ，如果sum > 10的话 = 1， 如果sum < 10的话 = 0
2. while 的判断条件， 因为我们已经对num1,num2,next都进行无效则= 0操作，所以我们可以在一个while里跑完
"""