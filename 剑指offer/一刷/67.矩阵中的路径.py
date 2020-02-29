class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # 标志位，初始化为false
        flag = [False]*len(matrix)
        for i in range(rows):
            for j in range(cols):
                # 循环遍历二维数组，找到起点等于str第一个元素的值，再递归判断四周是否有符合条件的 - ---回溯法
                if self.judge(matrix,i,j,rows,cols,flag,path,0):
                    return True
        return False

    # judge(初始矩阵，索引行坐标i，索引纵坐标j，矩阵行数，矩阵列数，待判断的字符串，字符串索引初始为0即先判断字符串的第一位)
    def judge(self,matrix,i,j,rows,cols,flag,path,k):
        # 先根据i和j计算匹配的第一个元素转为一维数组的位置
        index = i*cols + j

        # 递归终止条件
        if ( i < 0 or j < 0 or i >= rows or j >= cols or matrix[index] != path[k] or flag[index] == True):
            return False

        # 若k已经到达str末尾了，说明之前的都已经匹配成功了，直接返回true即可
        if (k == len(path)-1):
            return True

        # 要走的第一个位置置为true，表示已经走过了
        flag[index] = True

        # 回溯，递归寻找，每次找到了就给k加一，找不到，还原
        if(    self.judge(matrix,i-1,j,rows,cols,flag,path,k+1) or
               self.judge(matrix, i + 1, j, rows, cols, flag, path, k + 1) or
               self.judge(matrix, i, j-1, rows, cols, flag, path, k + 1) or
               self.judge(matrix, i, j+1, rows, cols, flag, path, k + 1) ):
            return True

        # 走到这，说明这一条路不通，还原，再试其他的路径
        flag[index] = False
        return False




if __name__ == "__main__":
    solution = Solution()
    print(solution.hasPath("ABCESFCSADEE",3,4,"ABCB"))



"""
感觉这题得用bfs来做吧？
没啥想法，感觉就是走了每一步，看看他的上下左右是否有对应的元素，如果有的话就走，没有的话就算了

答案比较复杂：
回溯
基本思想：
0.根据给定数组，初始化一个标志位数组，初始化为false，表示未走过，true表示已经走过，不能走第二次
1.根据行数和列数，遍历数组，先找到一个与str字符串的第一个元素相匹配的矩阵元素，进入judge
2.根据i和j先确定一维数组的位置，因为给定的matrix是一个一维数组
3.确定递归终止条件：越界，当前找到的矩阵值不等于数组对应位置的值，已经走过的，这三类情况，都直接false，说明这条路不通
4.若k，就是待判定的字符串str的索引已经判断到了最后一位，此时说明是匹配成功的
5.下面就是本题的精髓，递归不断地寻找周围四个格子是否符合条件，只要有一个格子符合条件，就继续再找这个符合条件的格子的四周是否存在符合条件的格子，直到k到达末尾或者不满足递归条件就停止。
6.走到这一步，说明本次是不成功的，我们要还原一下标志位数组index处的标志位，进入下一轮的判断。
"""