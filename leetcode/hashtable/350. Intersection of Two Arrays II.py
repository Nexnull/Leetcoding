"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
重复元素都要输入进res
"""
class Solution(object):
    def intersect(self, nums1, nums2):
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
                map[j] -= 1

        return res

"""
写的时候，我把map[j] = 0的判断条件删掉后（允许重复），只有一种case过不了
[4,9,5]
[9,4,9,8,4]

我输出的是:[9,4,9,4]
 expected:[9,4]

所以这时我就知道我们应该要对插入答案的次数进行限制
1.我们在map中已经记录了nums1每个元素的出现此时
2.在跑nums2的时候，每找到一个相同元素，就在字典中把该元素的出现次数减去1
这样就能保证插入答案的数，不超过任何一个列表的出现次数
"""