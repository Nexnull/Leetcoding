class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        stack = []
        length = len(nums)

        for i in range(2*length - 1, -1, -1):
            cur = nums[i%length]
            while len(stack) != 0 and cur >= stack[-1]:
                stack.pop()

            res[i % length] = -1 if len(stack) == 0 else stack[-1]
            stack.append(cur)

        return res

"""
https://www.youtube.com/watch?v=5IAq5jd8O7Y
答案：
1.做法与I 基本一样，但是这里多了重复
  例如 [1,2,1]
  在1的话，答案是[2,-1,-1]
  在这里， 答案是[2,-1,2] 因为这里的最后一个1与第一个1功用一个更大元素
  
2.所以我们要预想 把两个相同数组拼接起来， [1,2,1,1,2,1]。这样我们使用单调栈的时候就能
保证元素都能共享到相同的更大元素
3.做法使用 [i%length], i 的范围为[0,2*length-1]
3.这里要注意一个， cur >= stack[-1],stack.pop() 
  因为例如[1,2,1,1,2,1]这种情况 ， 假如说=不pop,那么单调栈会变成[1,2,2]，2的下一个最大元素就是2
  了，这样是错的


"""