class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return
        res = "1"

        for _ in range(1, n):
            count = 0
            pre = "."
            temp = ""

            for i in range(len(res)):
                # 假如说[i+1] == [i], 或者[0], count ++
                if res[i] == pre or pre == ".":
                    count += 1
                # 假如说[i+1] != [i]
                else:
                    temp += str(count) + pre
                    count = 1

                # 准备进入下一次循环，我们要把pre换成当前[i]
                pre = res[i]

            # 出了最后一次循环，需要最后处理一次
            temp += str(count) + pre
            res = temp

        return res


"""
https://www.youtube.com/watch?v=hTwR5lpjU-0
主要讨论两种情况
1.假如说[i+1] == [i], 那么count +=1, pre不变
2.假如说[i+1] != [i], 那么count要变回1， pre要变成[i]

然后在每次 [i+1] != [i] 都要把之前的处理结果加到temp
出循环后，我们把最后一次处理结果放进temp

然后更新res, 准备进入下一个n的处理
"""
