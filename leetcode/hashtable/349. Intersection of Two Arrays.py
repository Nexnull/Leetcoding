"""
Given two arrays, write a function to compute their intersection（交集）.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
重复元素不要输入进res
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = 1 if i not in map else map[i]+1

        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0

        return res

"""
Time:O(n) space:O(n)
这题可以使用多种方法来做，包括hash-table, two pointers, binary search
这里就只选用hash-table的方法来做把：
答案：
1.首先我们先把nums1给操作住：如果元素在map里，那么map[i] += 1
                          如果元素不在map里，那么map[i] = 1(新建立hash-set)
2.然后再操作nums2
假如说j 在map里，且map[j]>0（这个是避免多次把相同元素加入进答案里）: res.append(j)
                                                               map[j] = 0(这样保证元素不会被重复添加）


"""