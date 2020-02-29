# 同一个任务之间，我们执行的时候中间有n个任务的时间间隔，问我们总共需要使用多少时间
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks or len(tasks) == 0: return 0

        record = [0] * 26
        for item in tasks:
            record[ord(item) - ord("A")] += 1

        #为了得出那个任务的数量最多，根据这个来构造我们的table
        record = sorted(record)
        max_col = record[25] - 1
        # 构造table
        space = max_col * n

        for i in range(24, -1, -1):
            if record[i] > 0:
                # 减去有任务的格子，余下的都是休息部分
                space -= min(max_col, record[i])

        # 假如休息部分>0 , 说明我们直接用原有的任务量加上休息空间就好了
        if space > 0: return len(tasks) + space
        # 假如说没有休息空间，就说明任务刚好合理分配，直接返回就好了
        return len(tasks)

"""
https://www.youtube.com/watch?v=OQKpjr13VNk
"""