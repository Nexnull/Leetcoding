class Solution:
    def __init__(self):
        # 因为最大数据规模是1000
        self.par = [i for i in range(1001)]
        self.rank = [0 for _ in range(1001)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, p, q):
        p, q = self.find(p), self.find(q)
        if p == q:
            return
        else:
            self.par[q] = p
            if self.rank[p] == self.rank[q]:
                self.rank[p] += 1

    # 存在一个集合，假如说集合里有两个点已经存在，此时存在一条边能连接两者，那么能形成环
    # 我们把每次的边上的两个点，都查找他们的最父节点，假如说最父节点相同，说明他们是再同一个节点上
    # 若不是，那么我们则把他们合并到同一个集合里去
    def findRedundantConnection(self, edges):
        for e in edges:
            x, y = e[0], e[1]
            if self.find(x) == self.find(y):
                return [x, y]
            else:
                self.union(x, y)
        return []

"""
https://leetcode-cn.com/problems/redundant-connection/solution/bing-cha-ji-shui-ti-by-desgard_duan/
"""
