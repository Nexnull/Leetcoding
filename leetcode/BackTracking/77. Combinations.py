class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1: return []
        self.res = []
        self.helper(n, [], 1, k)
        return self.res

    def helper(self, nums, temp, cur, request_len):
        if len(temp) == request_len:
            self.res.append(temp[:])
            return

        for i in range(cur, nums + 1):
            temp.append(i)
            self.helper(nums, temp, i + 1, request_len)
            temp.pop(-1)
"""
https://www.youtube.com/watch?v=mlmpQB_yJfc
"""