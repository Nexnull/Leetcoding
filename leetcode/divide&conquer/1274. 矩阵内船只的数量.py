"""
在用笛卡尔坐标系表示的二维海平面上，有一些船。每一艘船都在一个整数点上，且每一个整数点最多只有 1 艘船。

有一个函数 Sea.hasShips(topRight, bottomLeft) ，输入参数为右上角和左下角两个点的坐标，当且仅当这两个点所表示的矩形区域（包含边界）内至少有一艘船时，这个函数才返回 true ，否则返回 false 。

给你矩形的右上角 topRight 和左下角 bottomLeft 的坐标，请你返回此矩形内船只的数目。题目保证矩形内 至多只有 10 艘船。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ships-in-a-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        x1, y1 = topRight.x, topRight.y
        x2, y2 = bottomLeft.x, bottomLeft.y

        # 越界处理以及看当前未知有没有船
        if x1 < x2 or y1 < y2 or not sea.hasShips(topRight, bottomLeft):
            return 0

        # 分割到最小点了但依然没被sae.hasShips给晒掉，说明这个点有船
        if (x1, y1) == (x2, y2):
            return 1

        # 开始二分
        xmid = (x1 + x2) // 2
        ymid = (y1 + y2) // 2

        # 注意有些边被处理过了，下次分块的时候有注意+1，-1
        return self.countShips(sea, Point(xmid, ymid), Point(x2, y2)) + \
               self.countShips(sea, Point(xmid, y1), Point(x2, ymid + 1)) + \
               self.countShips(sea, Point(x1, ymid), Point(xmid + 1, y2)) + \
               self.countShips(sea, Point(x1, y1), Point(xmid + 1, ymid + 1))

"""
分成不同的区块，然后递归查找
"""