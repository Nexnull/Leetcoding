class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums1)
        stack = []
        hashmap = {}

        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) != 0 and nums2[i] > stack[-1]:
                stack.pop()

            hashmap[nums2[i]] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums2[i])

        for i in range(len(nums1)):
            res[i] = hashmap[nums1[i]]

        return res

"""
https://www.youtube.com/watch?v=KZhjUwuMC0Y
答案：
本题目运用了一种新的数据结构（单调栈），它的作用是，能把一串数组放入，会形成一个单调递增的
样子（不是排序，会把不满足单调递增的元素给删除）

1.因为nums1 是nums2的子集，且我们想找到nums1每个元素所对应的下一个更大的元素，我们就得
想把nums2的每个下一个最大的元素找出来，然后存到map里去

2.所以我们要实现一个单调栈，完成栈之后，直接对比，把下一个元素放进去存进去
  例如 nums2 = [1,3,4,2]
     单调栈  = [1,3,4]
     所以对应的下一个元素为 {1:3 , 3:4, 4:-1, 2:-1} (不存在为-1)
     nums1 = [4,1,2] -> [-1,3,-1]

3.实现单调栈的方法是，
  每一次从数组拿到一个元素，先跟栈顶元素比大小， 大，则pop 栈，一直pop到栈顶元素比元素大
                                           小，则push

4.对于这题，在新元素加进 单调栈之前，我们需要先把它给加进字典，如stack还有元素，说明stack[-1]
                                                        就是nums[i]的下一个大元素
                                                        若没有元素 dic[nums[i]] = -1
"""