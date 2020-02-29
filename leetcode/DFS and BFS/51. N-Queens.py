"""
八皇后问题
若一个皇后在中间则它的的上下左右撇捺都无法放另一个皇后
   X X Q X X
   。X X X 。
   X 。X 。X

"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:return []
        self.result = []
        self.col = set(); self.pie = set(); self.na = set()
        self.DFS(n,0,[])
        return self._generate_res(n)

    def DFS(self,n,row,cur_state):
        if row >= n:
            self.result.append(cur_state)
            return

        for col in range(n):
            if col in self.col or (row+col) in self.pie or (row-col) in self.na:
                #该地方不能放置皇后
                continue

            #可以尝试放一下
            self.col.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n,row + 1, cur_state + [col])

            #消除当前皇后所造成的影响，为下一个皇后的尝试做好准备
            self.col.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)



    def _generate_res(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i   + "Q" + "."*(n-i-1))
        return [board[i:i+n] for i in range(0,len(board),n)]

"""
https://www.youtube.com/watch?v=3FWt0AeYT40&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=33
N皇后问题
1。先确立我们放置皇后的规律，是一层一层得往下面尝试
2。第一层，我们先把不能放置的地方排除掉（剪枝），然后挑一个位置，把皇后放上去试试（DFS and BFS）
3。皇后放上去之后，我们递归，往下一层走，看看下一层哪里可以放皇后，然后循环 2-3步

4。当我们发现，放置的皇后都没有问题。我们就来到了递归终止条件row >= n: ，然后把记录每层皇后index的list，加进res
5。若放置皇后的位置有问题，则进入下一个横坐标再尝试

6。假如说，我们第一次放皇后的位置index1，可以一直走出结果。然后终止递归，
    则我们同样需要消除index1放置皇后的影响
    同时for 循环还在继续，更新出下一个横坐标index2后，我们继续探索其他可以完成的答案（DFS and BFS）

代码问题：
1。因为我们是按层来往下递归，所以row我们就不用设变量了
2。因为set()的查找删除比list要方便的多，我们这里用set
3。至于储存在set里的元素， col, pie, na 的坐标是有依据的， 一pie，那一条线，刚好坐标都是等于row+col
                                                        na，那一条线，刚好都是等于row-col

"""