
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        #怎么去掉”01“里面的0的
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]

        for i in range(max(len(versions1), len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0


"""
https://www.youtube.com/watch?v=ycgUISujdMI
其实这题的主要思想就是，我们把点去掉，然后一位一位的比较
1.假如说出现 “1.22” 和 “1.2”这种情况， 我们就默认帮“1.2”补一个0
2.假如说出现“01" 这种，我们要把已开头的0去掉，至于
"""