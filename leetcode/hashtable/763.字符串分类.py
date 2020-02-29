"""
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_index = [0 for i in range(128)]

        for i in range(len(S)):
            last_index[ord(S[i])] = i

        res = []
        start = 0
        last = 0
        for i in range(len(S)):

            last = max(last, last_index[ord(S[i])])

            if i == last:
                res.append(last - start + 1)
                start = last + 1

        return res

"""
https://www.youtube.com/watch?v=s-1W5FDJ0lw
Time:O(n) Space:O(n)
我们先遍历一遍字符串，把每个char在字符串中出现的最后位置给记录在last_index中
然后我们创两个指针， start-last 之间就是一个区间
我们每个区间都去查找区间字母最远的范围，记录为last
然后当i遍历到这个最远范围时，就应该把这个给记录在res里面了， 记住，在这里start = last + 1,因为两个区间不能重叠
"""