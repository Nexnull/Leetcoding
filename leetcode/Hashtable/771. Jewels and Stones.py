class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if not J or not S: return 0

        hashmap = [False] * 256

        for char in J:
            hashmap[ord(char)] = True

        res = 0
        for char in S:
            if hashmap[ord(char)] == True:
                res += 1
        return res

"""
https://algocasts.io/episodes/VXGOxEpQ
Time: O(m+n), Space: O(k)
答案：这题做法和242的做法非常相似，都是创建一个hash来记录
1.首先创建一个256位的hash表
2.遍历珠宝，把对应的ord都变成True
3.遍历石头，检查石头所对应的index是否为True,如True的话则 res ++

"""