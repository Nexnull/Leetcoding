def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return False
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False

def containsDuplicate2(self, nums):
    if not nums:
        return False

    new = list(set(nums))
    if len(new) == len(nums):
        return False
    return True
"""
Time: O(n*log(n)), Space: O(1)
排序一遍，前后对比看有没相同

Time: O(n), Space: O(n)
集合过滤一遍，看与原来长度想不想等
"""
