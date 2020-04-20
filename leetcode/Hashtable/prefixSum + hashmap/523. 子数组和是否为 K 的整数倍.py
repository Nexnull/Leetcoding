class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False

        # key: sum%k value:index
        map = {}

        # 初始化，sum=0, index = -1
        map[0] = -1

        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

            # 语法不允许mod0, 所以当k=0的时候key = sum
            # 否则 key = sum%k
            # 因为 a = b(modk), 那么 a - b = m*k
            mod = sum if k == 0 else sum % k

            # 看mod在不在map.keys()里面
            if mod in map:
                j = map[mod]

                # 子数组要求长度至少为2
                # 这里和一般的数组下标减法不太一样。 正常[0,1] 1-0=1, 相差1，但有两个元素
                # 前缀和，[0,1,2,3,4], 4 -2 =2, [3,4]
                if i - j >= 2:
                    return True
            # mod不在map.keys()里面的话，那么就要把当前mod，index给加进去
            else:
                map[mod] = i

        return False

"""
https://algocasts.io/episodes/dlWbkomv
Time: O(n), Space: O(k)
这里主要有一个数学规律，然后其余的都是利用前缀和的做法
规律是  a (modk) = b (modk), 然后 a - b = m*k
所以这个题我们就是要找到两个mod后相等的数，然后把他们的下标找出来，取这个范围就可

"""


