"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Given input matrix =
[ [1,2,3],
  [4,5,6],
  [7,8,9]],
rotate the input matrix in-place such that it becomes:
[ [7,4,1],
  [8,5,2],
  [9,6,3]]
把矩阵顺时针旋转90度
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

"""
注意，python 的reverse是inplace的
https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image

这里的一个trick, 关于for循环的
for i in range(len(matrix)):
    for j in range(i,len(matrix[0])):
这样写其实遍历的是对称轴右半边的
   1 2 3 
   0 5 6 
   0 0 9 

for i in range(len(matrix)):
    for j in range(i+1,len(matrix[0])):
这样写的话能直接排除掉中轴上的，能节省一般的位置
   0 2 3 
   0 0 6 
   0 0 0 

/*
 * clockwise rotate(顺时针旋转90度的方法)
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/

/*
 * anticlockwise rotate逆时针旋转九十度的方法
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/

"""