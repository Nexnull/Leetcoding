class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""

        # 因为一开始可能会出现 "/////C/A" 这种多重斜杠的情况，所以我们把斜杠去掉
        # 然后去掉斜杠后原位置会出现 空格
        path = path.split("/")
        res = []

        for char in path:
            if char == "..":
                if len(res) > 0:
                    res.pop(-1)
            elif char != "." and char != "":
                res.append(char)

        return "/" + "/".join(res)

"""
https://leetcode-cn.com/problems/simplify-path/solution/zhan-by-powcai/代码
https://www.youtube.com/watch?v=l-og2X5GibY思路

这题的逻辑就是
.. 代表返回上一层
. 表示呆在这一层，不操作
字母代表层数
最后我们按层的要求把字符串输出

所以操作方法是
遇到字母，那么把字母加进结果
遇到.., 要是不可以pop了，就不处理，要是有元素，那就pop


"""