class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        # key ----> val， 当前元素的出度是是什么（当前元素指向什么元素）
        child = {}

        # val ----> key, 当前元素的入度是什么（当前元素被什么元素指向）
        par = {}

        for word in words:
            for char in word:
                child[char] = set()
                par[char] = set()

        # word1是上一个单词， word2是下一个单词
        for word1, word2 in zip(words[:-1], words[1:]):
            # 假如两个单词存在包含关系，那么是不可以检测的 例如"abc", "ab"
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""

            # 我们把单词之间的关系给放进child, par里：
            # 找出两个单词第一个不一样的字母， 那么上面的字母就是父，下面的字母就子
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    child[char1].add(char2)
                    par[char2].add(char1)

        # 下面进行拓扑排序, 拓扑排序是把 入度为0的节点给取出来, par[i] == 0
        # 然后把这个节点指向的元素，都去掉连接 char[node]
        res = []
        queue = []

        # 找到第一批入度为0 的节点
        list_no_par_node = [i for i in par if len(par[i]) == 0]
        for node in list_no_par_node:
            # 把入度为0的元素删掉，同时把它加进queue,准备去除它对别的node的影响
            del par[node]
            queue.append(node)

        while queue:

            node = queue.pop(0)
            res.append(node)

            # 把这个node的所有children拿出来，我们要把node -> child这种连接关系给去掉
            children = child[node]
            for ch in children:
                par[ch].remove(node)

                # 再把父-->child的连接删掉以后，我们要检查child当前是不是入度为0，为0的话我们要把它加进queue,下一步处理
                if len(par[ch]) == 0:
                    queue.append(ch)
                    del par[ch]

        print(queue)
        if par:
            return ""
        return "".join(res)
"""
https://www.youtube.com/channel/UCCMpGENpr93ENbfdinP3QeQ/about
有bug， ["za","zb","ca","cb"])这个测试条件过不了

"""
solution = Solution()
solution.alienOrder(["za","zb","ca","cb"])
# solution.alienOrder(["wrt","wrf","er","ett","rftt"])

