class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        wordList = set(wordList)
        visited = set()

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist

            for i in xrange(len(word)):
                for j in ls:
                    if j != word[i]:
                        newWord = word[:i] + j + word[i + 1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist + 1))
                            visited.add(newWord)
        return 0

"""
上面的做法用的是单向BFS，时间复杂度比较高
思路：https://www.youtube.com/watch?v=vWPCm69MSfs

ls = string.ascii_lowercase代表26个小写字母
wordList = set(wordList)，避免单词重复出现的情况，提升了效率
"""