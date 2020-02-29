"""
问跳到数组最后最少需要几次
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return False
        if len(nums) == 1:return 0
        n = len(nums)
        maxindex = 0

        jump = 0; curEnd = 0

        for i in range(n):
            if maxindex >= n-1: return jump + 1
            if i > maxindex: return -1

            if i > curEnd:
                jump += 1
                curEnd = maxindex

            maxindex = max(maxindex,i+nums[i])
        return -1

"""
https://algocasts.io/episodesaAEpo1vmQ
Time: O(n), Space: O(1)
答案：
jump 表示跳到i所需要的最小步数
curEnd 表示，当前步数(jump)所能跳到的最远距离
maxindex 表示在可走范围内，所能跳到的最远距离
所以我们在遍历到i > curEnd的时候，说明了再远的话，就需要再跳了
然后再跳一步的话，curEnd就等于下一步的最远距离maxindex
"""

#Time: O(n), Space: O(n)
def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None or len(nums) == 0: return -1

    n = len(nums)
    maxindex = 0
    step = [0] * n

    for i in xrange(n):
        if maxindex >= n - 1: return step[n - 1]
        if i > maxindex: return -1
        maxindex = i + nums[i] if i + nums[i] > maxindex else maxindex
        last = maxindex if maxindex < n - 1 else n - 1
        for j in xrange(last, i, -1):
            if step[j] != 0:
                break
            step[j] = step[i] + 1

    return -1