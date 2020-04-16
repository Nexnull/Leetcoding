class Solution:
    def lexicalOrder(self, n):
        res = []
        # 对每棵树进行dfs
        for i in range(1, 10):
            self.dfs(i, n, res)
        return res

    def dfs(self, cur, n, res):  # cur为根结点
        # 说明当前数字超出最大范围了,跳过
        if cur > n:
            return
            # 说明cur 还没有超出最大范围
        else:
            res.append(cur)

            # 然后对cur继续进行下一层的遍历
            for i in range(10):
                # 比如叶子结点为14，而n是13，dfs就结束了
                if 10 * cur + i > n:
                    return
                self.dfs(10 * cur + i, n, res)

"""
关于这种题，我们要始终了解什么叫字典序
           1              2      3
   10  11 12 13...19 
100 101 ...  198   199

所以最好的做法是对单个数字进行dfs, 然后然后看看有没超范围，没超的话就一直做dfs

时间复杂度：o(N) 空间复杂度 ??
https://leetcode-cn.com/problems/lexicographical-numbers/solution/386zi-dian-xu-pai-shu-python-by-ml-zimingmeng/
"""