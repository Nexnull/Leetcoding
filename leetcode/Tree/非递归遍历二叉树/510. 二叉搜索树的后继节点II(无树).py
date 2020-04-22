"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 加入该节点有右节点，那么就找右节点的最左节点
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # 加入该节点无有右节点，说明下面不可能有下一个顺序节点
        # 那么我们要向上找，找到该节点的位置是属于根节点的左节点，那么下一个节点就是根节点了
        while node.parent and node == node.parent.right:
            node = node.parent

        return node.parent

"""
https://leetcode-cn.com/problems/inorder-successor-in-bst-ii/solution/er-cha-sou-suo-shu-zhong-de-zhong-xu-hou-ji-ii-by-/

时间复杂度：O(H)。其中H为树的高度。平均时间复杂度为 Olog N，最坏的事件复杂度为 O(N)，
其中 N 为树的结点数。
空间复杂度：O(1)，在计算的过程中没有使用额外空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/inorder-successor-in-bst-ii/solution/er-cha-sou-suo-shu-zhong-de-zhong-xu-hou-ji-ii-by-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

算法：
1。若 node 结点有右孩子，则它的后继在树中相对较低的位置。
        我们向右走一次，再尽可能的向左走，返回最后所在的结点。
2。若 node 结点没有右孩子，则它的后继在树中相对较高的位置。
    我们向上走到直到结点 tmp 的左孩子是 node 的父节点时，则 node 的后继为 tmp。


"""