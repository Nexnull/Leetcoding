class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s or len(s) == 0: return []

        res = []
        for word in wordDict:
            if s.startswith(word) == False:
                continue
            if s == word:
                res.append(word)
            else:
                resultofRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultofRest:
                    temp = word + " " + item
                    res.append(temp)

        memo[s] = res
        return res

"""
这题已经不是我们前面看的那种简单的回溯了。也不能套用前面那些回溯的模版
https://www.youtube.com/watch?v=JqOIRBC0_9c
https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
答案：
其实这题是一步步拆分来做的
1.memo是一个字典，他的 key是s中的字符串，value是这个字符串能拆分成wordDict的什么形式(部分答案)
    例如： key = anddog , value = and dog || 
  它的作用是，记录当前字符串片段的可能分解(部分答案)

2.主循环里有一个res = [],准备保留着最终结果，然后for循环把dict里的每一个单词(word)都拿出来去尝试，
然后把,s - word部分再继续递归，试图返回一个部分结果的res （resultofRest），来与word进行拼接，来形成最终答案

3.剩下的一些都是一些为这些递归准备的限制条件
"""