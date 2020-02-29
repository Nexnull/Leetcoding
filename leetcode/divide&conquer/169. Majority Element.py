"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
求众数
"""
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        return max(count.keys(), key = count.get)

class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0

        res = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count = 1
            elif res == nums[i]:
                count += 1
            else: count -= 1

        return res


"""
https://algocasts.io/episodes/VlWd8W06
方法一：暴力解，一次次循环找出最大的数，O(n^2) 空间O(1)
方法二：用字典记录，然后找出最大的value，时间空间都为O（n)
方法三，把nums排序好，然后返回nums[len//2].因为众数的数量是大于等于一半的，所以
即使是极端情况，最小的数字是众数，那么nums[len//2]依旧能返回这个数，所以直接这样做
就可以了。时间 O(nlogn),空间O(1)

时间 O(n),空间O(1)
我们用res 来记录当前数量最多的数字
我们用count 来记录当前res记录的数字出现的次数，
遇到相同的数字，count 就加一， 遇到不相同的数字，count就-1
  nums[i] == res: count ++
  nums[i] != res: count --
  if count == 0:
        res = nums[i]
        count = 1
    
"""