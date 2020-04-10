# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        d = 0
        node = root
        # root节点高度是0，我们首先先算出二叉树的高度
        while node.left:
            node = node.left
            d += 1

        # 然后我们在最下面一层做一个二分查找
        # 找到从左到右第一个不存在的node的下标
        l = 0
        r = 2 ** d - 1
        # 因为我们设置内部终止条件，所以只能使用 while循环的条件不满足来退出
        # 一般是用while 循环退出的话， l都会指向右边。r会指向左边，所以退出时l指向的是不存在的第一位
        while l <= r:
            mid = (l + r) // 2
            if self.exist(mid, d, root):
                l = mid + 1
            else:
                r = mid - 1

        return (2 ** d - 1) + l

    def exist(self, index, depth, root):
        l = 0
        r = 2 ** depth - 1

        # 因为我们要从最上一层往下找,每次看index在整个区间的范围是左还是右
        # 来决定接下来的路要怎么走
        for _ in range(depth):
            mid = (l + r) // 2
            # index是外面的二分查找的中点,我们要看这个点存不存在
            # 所以移动的趋势要按照这个点来移动
            # 例如(4,5) (6)
            # mid=1
            # index = 0,1的话， right = mid
            # index = 2的话， left = mid+1
            if mid < index:
                root = root.right
                l = mid + 1
            # 如上面的情况 index = mid的时候，其实还是在左边的
            elif index <= mid:
                root = root.left
                r = mid

        return root is not None

"""
https://www.youtube.com/watch?v=rvZfvo-r5WU
视频对这个二分查找讲的特别详细
"""