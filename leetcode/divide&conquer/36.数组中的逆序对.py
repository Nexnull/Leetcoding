class Solution:
    def InversePairs(self, data):

        list,count = self.MergeSort(data)
        return count%1000000007

    def MergeSort(self,data):

        totalLen = len(data)

        if totalLen == 1:
            return data,0

        part1, part2 = data[:totalLen//2],data[totalLen//2:]
        sorted_part1,count1 = self.MergeSort(part1)
        sorted_part2,count2 = self.MergeSort(part2)

        sorted_total = sorted_part1+sorted_part2
        count3 = 0

        p = 0
        q = sorted_total.index(sorted_part2[0])
        len_first = len(sorted_part1)
        len_last = len(sorted_total)

        #关键的计数在这里
        while p < len_first and q < len_last:
            while p < len_first:
                #因为sorted total是两个排好序的放在了一起，所以只要有一个大于，则其余的全部大于
                if sorted_total[q] < sorted_total[p]:
                    count3 += len_first - p
                    break
                p += 1
            q += 1


        returnList = []
        p,q = 0,sorted_total.index(sorted_part2[0])
        while p < len_first and q < len_last:
            if sorted_total[p] < sorted_total[q]:
                returnList.append(sorted_total[p])
                p += 1
            else:
                returnList.append(sorted_total[q])
                q += 1

        if p == len_first:
            returnList += sorted_total[q:]
        if q == len_last:
            returnList += sorted_part1[p:]

        return returnList, count3 + count1 + count2





if __name__ == "__main__":
    solution = Solution()
    solution.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575])



"""
https://algocasts.io/episodes/qjG0K8mK
Time: O(n*log(n)), Space: O(n)
正确思路：
这题使用了merge sort的思想
例如:  8 2 4 7
1.  我们把它拆开变成 8 2   4 7
    然后先把两个数组分别排序，并拿到他们的count
    82 -> 28,count=1    47->47,count=1
    
    count1, count2 表示，在82 和 47，这两对里面各自有多少逆序对
    count3表示 前面和后面，能产生多少个逆序对
    所以count1 count2 count3加起来就是8247所有的逆序对了
    

2.为什么要左右数组排序后，再进行count3的对比呢？
    视频中 3 分 10 秒那里开始就讲了为什么要排序。
    不排序就只能暴力穷举(On^2)，排序就是为了降低时间复杂度。O(n)
"""