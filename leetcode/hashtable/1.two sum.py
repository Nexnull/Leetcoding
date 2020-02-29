"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hashmap.keys():
                return [i, hashmap[rest]]

            hashmap[nums[i]] = i
        return []


if __name__ == "__main__":
    solution = Solution()
    solution.twoSum([3,3],6)


"""
写的时候是没什么大问题，但是有个问题我解决不了，就是当出现[3,3] 6这种情况，我们怎么能保证
set的查找出来的是index为另一个3呢

答案：
1。所以在这里，视频的那个人讲的是有错误的
这里应该用hashtable来写，不应该用set,因为hashtable每次可以记录
元素及其下标，例如[3,3]这个例子，假如说遍历到第二个3，且我们
可以判断出来了m in d,那么返回的下标必不可能是当前数字的下标

2。这题两个做法，一是暴力解，遍历到一个数就开始遍历整个列表
看看能不能跟target匹配上的，O(n^2)
第二种解法是利用字典来做，查看当前遍历到的数字n, target - n是否在字典里，在的话就返回，不在话添加n进字典
遍历数组和字典存储时间 O(n)*O(1)

3.注意：千万不能先把nums[i]添加到字典里再判断，例如6 [3,2,4]这种情况
  假如说你先把3给加进map里面去了，你去执行if 判断会发现3也在里面，那么直接就返回答案了

"""
