"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors
把一个图的节点和边都复制出来
"""

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def __init__(self):
        self.map = {}
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None: return


        copy = Node(node.val,[])
        self.map[node] = copy

        for n in node.neighbors:
            if n in self.map.keys():
                copy.neighbors.append(self.map[n])
            else:
                copy.neighbors.append(self.cloneGraph(n))
        return copy

"""
为什么在这题一定要先验证一个元素是否在map里，才把它加进node.neighbors呢？
能不能解释一下这样做的必要性？

map 里存储的对应关系是原图的 node 和复制的 node，如果某个 node 不在 map 中，
说明这个 node 还没处理过，也即还未对这个 node 进行复制，（self.map[node] = copy）
自然是拿不出拷贝的 node 加到拷贝图里的。所以要先递归去处理这个未处理过的 node。
最后return copy也就是把这个node处理完后再丢回进neighbors


注意：
1.copy.neighbors.append(self.map[n])，这里的append，必须append出新建的node,要不然
就不能称之为是deepcopy了
"""