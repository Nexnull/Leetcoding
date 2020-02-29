"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words
exactly once and without any intervening(介于中间的) characters.


Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting（开始坐标） at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
"""
from collections import Counter
from copy import deepcopy
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []

        res = []
        words_count = len(words)
        # words的每个单词的长度都相同，我们待会切片就用这个长度来切
        word_len = len(words[0])
        hashmap = Counter(words)

        # barfoothefoobarman
        #             i(i最多找到这就可以了) -> 这个位置是len(s) - words_count*word_len + 1
        # i 作为左指针，只要找到单词组合的第一个字母就行了，因为我们会对i后面的每个单词组都排查一遍，所以没必要遍历整个s
        for i in range(len(s) - words_count * word_len + 1):
            # 每次循环我们都赋予 copy 一个新hashmap,这样我们就不用考虑我们探索时候对hashmap造成的影响
            copy = deepcopy(hashmap)
            k = words_count
            j = i
            while k > 0:
                # 我们把str 切分成一个单词。例如"foo"
                str = s[j: j + word_len]

                # 然后看这个单词在不在hashmap里面，如果不在说明这个区间内根本不可能满足找到words的条件
                if str not in copy or copy[str] < 1:
                    break

                # 如果有这个单词的话，我们就把hashmap对应的key --
                # 然后把 还需要的单词数量k  -= 1
                # j += word_len, 去查看下一个字符串块
                copy[str] -= 1
                k -= 1
                j += word_len

            # 最后发现我们需要的单词数量找完了，就把当前的头index : i 给放进res
            if k == 0: res.append(i)
        return res

"""
https://www.youtube.com/watch?v=L6NLra-rZoU
time:O(n^2) space O(n)
答案：
切片 + hashmap
"""


