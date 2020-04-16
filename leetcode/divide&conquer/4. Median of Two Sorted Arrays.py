class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        # 这里的 k并不是index，而是第几个数
        if total & 1 == 1:
            return self.findKthsmallnumber(nums1,nums2,total//2 + 1)
        else:
            a = self.findKthsmallnumber(nums1,nums2,total//2)
            b = self.findKthsmallnumber(nums1,nums2,total//2 + 1)

            return (a+b)//2.0



    def findKthsmallnumber(self,nums1,nums2,k):
        len1, len2 = len(nums1), len(nums2)
        # p1,p2表示的是数组的偏移量，p左边的元素就表示已经被排除了
        pointer1, pointer2 = 0, 0

        while True:
            if len1 == 0:return nums2[pointer2 + k - 1]
            if len2 == 0:return nums1[pointer1 + k - 1]

            # 例如 [1,3] [2] 这种情况
            # 1被排除后，指针分别指向2，3
            # 那么我们当然是取小的那一个了
            if k == 1:return min(nums1[pointer1],nums2[pointer2])

            # 取nums1的第k/2个数,那么nums2要取的数就是 k/2 - i,
            # 因为我们每个数组要刚好取出 k/2个数
            i = min(k//2,len1)
            j = min(k-i,len2)

            # 把各自数组中第k/2个数给取出来
            num1_hk = nums1[pointer1+i-1]
            num2_hk = nums2[pointer2+j-1]

            #说明两个数组合并起来的话，第k个数和第k-1个数是相同的
            if i + j == k and num1_hk == num2_hk:
                return num1_hk

            if num1_hk <= num2_hk:
                #说明num1,的前k/2个数都是没用的，直接移动pointer1排除
                pointer1 += i
                len1 -= i
                k -= i

            if  num1_hk >= num2_hk:
                #说明num2,的前k/2个数都是没用的，直接移动pointer2排除
                pointer2 += j
                len2 -= j
                k -= j

            # 这里涉及到一个问题，为什么num1_hk <= num2_hk，这里可以等于
            # 因为当两数相等，且i + j 并没有到k, 例如len长度已经不够了，所以取len 而不是k-i,
            # 就说明在nums1[0..i],nums2[0..j]
            # 都不存在中位数，所以等于两个判断语句都执行了一遍
            # 把nums1[0..i],nums2[0..j]直接排除掉了


"""
https://algocasts.io/episodes/Qqpn6pkK
// Time: O(log(k)) <= O(log(m+n)), Space: O(1)
答案：
1.两个数组的长度和有可能为奇数有可能为偶数
奇数的话，那么直接返回总长度的 k//2+1就好了
偶数的话，需要放回总长度的 ([k//2] + [k//2+1])//2.0(因为5/2 == 2)所以要除2.0

2.pointer1,pointer2,表示从[pointer1..end]这个数组是还有效的
（因为我们后面涉及到删除操作）

3.i,j表示，把k 平均分到i,j 上，所以[pointer1+i-1]表示，在数组1，第k/2个数
"""

