"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.
给定两个单词，问在列表里面这两个单词的最短距离是多少
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        res = len(words)
        a, b = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                a = i
            if word == word2:
                b = i
            if a != -1 and b != -1:
                res = min(res, abs(a - b))
        return res

"""
给两个单词分配两个指针，当遍历到对应单词的时候，更新指针的值
然后当两个指针的值都更新过后，持续判断更新两指针的最小值
最后返回最小值
"""