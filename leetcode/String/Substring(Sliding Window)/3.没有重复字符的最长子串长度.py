
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        start = -1
        maxLen = 0

        for i in range(len(s)):
            # s[i] in hashmap
            # abca,start = -1 -> start = 1
            if s[i] in hashmap and hashmap[s[i]] > start:
                start = hashmap[s[i]]
                hashmap[s[i]] = i
            # s[i] not in hashmap
            else:
                hashmap[s[i]] = i
                if i - start > maxLen:
                    maxLen = i - start
        return maxLen

"""
https://www.youtube.com/watch?v=COVvQ9I7XyI
答案：
1.强调一点，这里计算长度的方式是 i - start, 这种计算方式是计算（start,i]的长度
所以一开始start 是等于-1，因为这样才可以计算从[0,i]的长度

2.我们一次遍历完整个字符串

    如果 s[i] 在之前出现过，**同时hashmap[s[i]] > start
    我们更新start,说明(start old, new start - 1]这一串都不要了
    要重新统计[new start,...]
    同时更新hashmap[s[i]]的value
    
    如果s[i] 没在之前出现过，**或者 hashmap[s[i]] < start
    说明这个元素我们愿意把它统计到最长子串中
    例如："tmmzuxt"
    
    我们愿意把最后一个t加入到我们的最长字串当中，因为第一个t我们早已不在字串中了（index<start)
    所以这个最后这个t我们要把它加进去
    
      
    
"""