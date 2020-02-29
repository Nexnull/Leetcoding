class Solution:
    def helper(self, sequence):
        if len(sequence) == 0:
            return True

        root = sequence[-1]
        flag = -1

        for i in range(len(sequence) -1):
            if sequence[i] > root:
                flag = i
                break

        for i in sequence[flag:-1]:
            if i < root:
                return False

        return self.helper(sequence[0:flag]) and self.helper(sequence[flag:-1])

    def VerifySquenceOfBST(self, sequence):

        if len(sequence) == 0:
            return False

        return self.helper(sequence)


if __name__ == "__main__":
    solution = Solution()
    solution.helper([4,6,7,5])

"""

一开始先是无什么想法

回顾一下二叉搜索树的基础：
    先序遍历：1。根节点
             2。左节点
             3。右节点
    所以导致输出的列表，【根节点，比根节点大的数，比根节点小的数】

    中序遍历：1。左节点
             2。根节点
             3。右节点
    所以导致输出的列表，【比根节点小的数,根节点，比根节点大的数】

    后序遍历：1。左节点
             2。右节点
             3。根节点
    所以导致输出的列表，【比根节点小的数,比根节点大的数，根节点】

现在这题是要看，输出的列表是否符合后序遍历的顺序，我们就可以根据后序遍历的
规律来进行查看了

1.找到root,并剔除root的影响
2，找到比根节点大，和比根节点小的分界点
3，分别这两个序列是否都比根节点大或都比根节点小（查看是否满足后序遍历的规律）
4，把这两个sequence继续递归分化，重复123的过程

debug点：
flag的初始值设定应该是sequence的最后以为，因为若flag = 0 ,然后对于【6，7】来说，无法更新flag,后进入判断就会
报错
"""