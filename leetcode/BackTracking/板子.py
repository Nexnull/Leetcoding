"""
通用板子
这个讲解讲的好 ßhttps://www.youtube.com/watch?v=zIY2BWdsbFs
"""
temp,nums,res= [],[],[]

class Solution(object):
    def main(self, nums):
        if not nums or len(nums) == 0: return []
        self.res = []
        self.helper(nums,[])
        return self.res

    def helper(self,nums,temp):
        # 1。append条件，取决于你想要输出的结果是什么
        if len(temp) == len(nums):
            self.res.append(temp[:])

        # 2.for 循环遍历，取决于你想要怎么添加元素
        # 3。在for循环开始部分添加过滤条件，过滤掉我们不需要的元素
        for i in range(len(nums)):
            temp.append(nums[i])
            self.helper(nums,temp)
            temp.pop(-1)

"""
1. append条件，取决于你想要输出的结果是什么
"""
#permutation,我们需要长度为得和条件数组一样的排列
    def helper():
        if len(temp) == len(nums):
            res.append(temp[:])

#subset，对temp的长度没有要求，反正满足subset就直接添加
    def helper():
            res.append(temp[:])

#combination,c(n,k),所以要求temp的长度为k
    def helper(request_len):
        if len(temp) == request_len:
            res.append(temp[:])
            return

#注意，为什么这里combinmation要return。permutaiton不需要return
# 这是根据他们的递归结构来决定的
# combination temp到达长度为k的时候，不return 则会继续走for 循环，产生不必要的计算
# permutation是因为len相等时，此时他的index 已经和len(nums)一样了，for i in range(index,len(nums))不会执行了
# 所以没必要

"""
# 2.for 循环遍历，取决于你想要怎么添加元素
"""

cur = 0
# permutation,A(n)(n).res中也是不能重复，但我们这里不是用for来去除这种情况
# 我们使用visited来确保temp里不含有重复的元素
# 这里是全排，所以就是temp里只要满足res不重复的组合，都得加一遍，所以不同于set，combination的处理情况
# 所以我们用visited来锁住位置，然后尝试所有元素都往剩下的位置放
def helper(self, nums, temp):
    for i in range(len(nums)):
        if self.visited[i]: continue
        self.visited[i] = True
        temp.append(nums[i])
        self.helper(nums, temp)
        self.visited[i] = False
        temp.pop(-1)


# subset，对temp要求元素不能重复，所以调用时i + 1
def helper(self, nums, temp, cur):
    for i in range(cur, len(nums)):
        temp.append(nums[i])
        self.helper(nums, temp, i + 1)
        temp.pop(-1)

# combination,c(n,k),由于对长度有限定（k)，且要求temp里面的数字不能重复，
# 所以都是从cur->nums+1,cur在每次调用都+1
def helper(self, nums, temp, cur, request_len):
    for i in range(cur, nums + 1):
        temp.append(i)
        self.helper(nums, temp, i + 1, request_len)
        temp.pop(-1)

"""
# 3.去重方法
1.subset2,和combination2都是同层去重法，这是答案结构决定的（添加下一个数时，只能从i+1开始添加）
2. permutation是全局去重法，因为它对添加下一个数是从（没被添加过的添加），所以只要是满足i > 0的都要判重

为什么subset,combination不用全局去重，因为全局去重筛选范围太大，有可能把答案给筛除掉
"""

# subset2
    def helper(self, nums, temp, cur):
        self.res.append(temp[:])

        for i in range(cur, len(nums)):
            if i > cur and nums[i] == nums[i - 1]: continue
            temp.append(nums[i])
            self.helper(nums, temp, i + 1)
            temp.pop(-1)

# combination2
    def helper(self, candidates, target, temp, cur):
        if target <  0:return
        if target == 0:
            self.res.append(temp[:])
            return

        for i in range(cur, len(candidates)):
            if i > cur and candidates[i] == candidates[i - 1]: continue
            temp.append(candidates[i])
            self.helper(candidates, target - candidates[i], temp, i+1)
            temp.pop(-1)

# permutations2
    def helper(self, nums, temp):
        if len(temp) == len(nums):
            self.res.append(temp[:])

        for i in range(len(nums)):
            if self.visited[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and self.visited[i - 1]:
                continue

            self.visited[i] = True
            temp.append(nums[i])
            self.helper(nums, temp)
            self.visited[i] = False
            temp.pop(-1)