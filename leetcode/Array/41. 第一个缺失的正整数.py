class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 1

        p = 0
        n = len(nums)
        while p < n:
            num = nums[p]
            if 1 <= num < n and nums[num - 1] != num:
                self.swap(nums, p, num - 1)
            else:
                p += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
https://algocasts.io/episodes/qjG0D8GK
Time: O(n), Space: O(1)
答案：
1.题目关键点，让每个index,都放上对应的数字，然后再检查对应的数字对不对，假如说不对的话，那么第一个不对的数字就是缺失的数字
  例如 应该 1  2  3
      实际 [1, 2, 0]
      放置好后：
          [1, 2, 0]
        发现 index(2) + 1 != 0,说明这个0的位置是错的，返回index+1(说明缺失了3）

2. 处理办法 nums[num-1] != num 
  例如num = 2, 他应该放在index 1上，所以
          nums[2-1] == 2,说明这个是放对的

3. 注意，我们这里因为是只放置正数（因为没有留index给负数和0），所以我们遇到负数和0的时候，指针直接跳过就好了
   不进行主动交换，因此我们有  1 <= num < n

此题可以和268题对照来看
"""