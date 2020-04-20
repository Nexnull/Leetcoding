"""
你要判断是否有可能上完所有课程
https://algocasts.io/episodes/rLmP3yWo
方法1，把所有课都转换成有向图，先修指向后修，然后进行dfs
假如说dfs都是可以终止的，说明没有环，也就说明了可以完成这些课：
有环，例如： 3的课需要2的前置，2的前置是3，所以这两门课永远没办法去上，
dfs到了这里也无法终结

checked[]:用来储存dfs结束的节点，说明这个点开始的路径无环

节点总数是V，边的总数是E,构造图花费V+E,遍历图也需要V+E
time(V+E) Space(V+E)

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。


"""
#方法1
class Solution(object):
    def hasCycle(self, graph, visited, checked, v):
        # visited被访问过了，说明有环，返回True
        if visited[v]:
            return True
        visited[v] = True

        # 判断v路径下的所有节点是否有环
        for i in graph[v]:
            if not checked[i] and self.hasCycle(graph, visited, checked, i):
                return True

        # 没有环，把v加进checked,然后在visited把v给还原下
        checked[v] = True
        visited[v] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]][后修，先修]
        :rtype: bool
        """
        if numCourses <= 1 or prerequisites is None or len(prerequisites) == 0:
            return True
        # 把每个课都创一个属于自己的list,list里存放着的都是当前index后修的课
        graph = [[] for i in range(numCourses)]

        # (0,1) 0<-1
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])

        # 初始化checked 和 visited
        checked = [False]*numCourses
        visited = [False]*numCourses

        # 检查每个课号，看他们的后修课是否有环
        for i in range(numCourses):
            if not checked[i] and self.hasCycle(graph,visited,checked,i):
                return False
        return True

"""
time(V+E) Space(V+E)
方法2：拓扑排序 = 顶点染色 + 记录顺序
入度，进入一个节点边的条数，称为入度
出度，出一个节点边的条数，称为出度
做法：先找出入度为0的点，然后把这个点的出度边都删除
     删除后，找出第二个入度为0的点，然后再把这个点的出度给删除
     ...
     我们按这样的节奏把所有入度为0的点给找出来
     然后？
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]][后修，先修]
        :rtype: bool
        """
        if numCourses <= 1 or prerequisites is None or len(prerequisites) == 0:
            return True

        # 把每个课都创一个属于自己的list,list里存放着的都是当前index后修的课
        graph = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        # (0,1) 1->0 变成[1] = append(0)，把后修的课append进先修的课index
        # 因为 1->0 , 所以0的indegree +1(初始化indegree)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1

        # 我们把indegree 为0的数找出来，作为我们图查询的起点
        q = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        # 当图查询没结束是，循环江一直进行
        count = 0
        while len(q) > 0:
            # 这个v已经是明确没有indegree了，功成身退，计入count中，然后再利用这个V来查询
            # 相邻的节点
            v = q.pop(0)
            count += 1
            for i in graph[v]:
                # 把v指向的节点的的入度减1，即是把v的入度去掉
                indegree[i] -= 1
                # 去完之后必有新的节点的入度为0，则继续用它来进行这个过程
                # 如果没有的话则循环结束，返回结果
                if indegree[i] == 0:
                    q.append(i)

        return count == numCourses

"""
remark:
这题即使不写判断边界条件也不会出错，因为我们在创造graph的时候，默认最差就是创造出一个
【】(num = 0)，然后即使这样进行下去，count == numcourses
"""



