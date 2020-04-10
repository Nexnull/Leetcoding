class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


"""
因为  0 是cold positon
     1,2,3 是hot positon
     4只能到 123，所以是cold
     5，6，7能到4,所以是hot
     所以我们发现，只要能被4整除的，都是cold position
"""