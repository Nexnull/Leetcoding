#资源：https://www.youtube.com/watch?v=oLtvUWpAnTQ&list=PLAnjpYDY-l8IacYv_2lIZxNrQmkY3paSN&index=2
"""
BFS：广度优先
元素进出：后进先出
数据结构：queue,pop(0)
探索规则是探索 与当前node有联系的所有结点

  / c - g
a - d
  \ e - f

遍历顺序：a c d e g f
那么它的探索规律应该是 第一层 a 第二层 cde 第三层 gf


BFS的写法其实就是每次扫描到一个元素，就把那个元素加进容器里
然后每次都pop（0），再扫描这个元素所关联的结点，其实就是我们做的二叉树层级遍历
然后储存BFS的容器是queue因为是从后面添加元素，从前面pop出元素
（但是我是用list来实现这个效果的）

"""

graph = {
    "A" : ["B","C"],
    "B" : ["A","C","D"],
    "C" : ["A","B","D","E"],
    "D" : ["B","C","E","F"],
    "E" : ["C","D"],
    "F" : ["D"]

}

def BFS(graph , s):
    queue = []
    queue.append(s)
    seen = set()#用来看哪些点已经被访问过
    seen.add(s)

    while len(queue) > 0:
        vertex = queue.pop(0)

        #把这个点的所有连接点放进queue里
        nodes = graph[vertex]

        for node in nodes:
            if node not in seen:
        #如果点没被访问过则加进queue
                queue.append(node)
                seen.add(node)
        print(vertex)

# BFS(graph,"A")


"""
DFS and BFS:深度优先
探索规则是探索 与当前node有联系的一个节点
  / c - g
a - d
  \ e - f
  
遍历顺序：a c g d e f

与BFS不同的地方在于，它是一条路黑到底，走完一条，慢慢回来
发现又有一条路，再继续往下走

元素进出：后进先出
数据结构：stack,pop(-1)
"""


def DFS(graph , s):
    stack = []
    stack.append(s)
    seen = set()#用来看哪些点已经被访问过
    seen.add(s)

    while len(stack) > 0:
        vertex = stack.pop(-1)

        #把这个点的所有连接点放进queue里
        nodes = graph[vertex]

        for node in nodes:
            if node not in seen:
        #如果点没被访问过则加进queue
                stack.append(node)
                seen.add(node)
        print(vertex)

DFS(graph,"A")