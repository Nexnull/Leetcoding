class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]

        adj = [set() for i in range(n)]

        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(len(adj)) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for i in leaves:
                # x元素在leaves
                # 首先把x的set里的元素清空
                j = adj[i].pop()
                # 其次再把拥有 x这个元素的set中,删掉x
                adj[j].remove(i)
                # 然后看这个拥有 x这个元素的set,的长度
                # 假如长度为1的话，有可能是下一轮处理，也有可能这就是答案
                if len(adj[j]) == 1: new_leaves.append(j)
            leaves = new_leaves
        return leaves
"""
思路：
https://algocasts.io/episodes/AwmXLzmx
https://www.youtube.com/watch?v=pUtxTz134qM
代码：https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
答案：
这里涉及到一个图的理论， 假如说你不知道的话这题是没办法做出来的（收缩法）
1.我们要不断删除，连接点只有1的点，删除到最后余下的点，都是长度最小的点
2.做法比较取巧
"""