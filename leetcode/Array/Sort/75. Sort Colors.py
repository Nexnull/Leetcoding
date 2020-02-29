"""
法国国旗问题，把0放最左边，把1放中间，把2放最右边
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums and len(nums) == 0: return []
        left = 0; mid = 0 ;right = len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                self.swap(left, mid, nums)
                left, mid = left + 1, mid + 1
            elif nums[mid] == 1:
                mid += 1
            else:
                self.swap(mid, right, nums)
                right -= 1
        return nums

    def swap(self, a, b, nums):
        nums[a], nums[b] = nums[b], nums[a]

"""
https://algocasts.io/episodes/aVWyAYW2
Time: O(n), Space: O(1)
这题有点三指针的感觉，left左边放的是0，right右边放的元素是2，mid在中间

1.mid查找，并把元素放到left,right的左右。
2.[mid] == 0, [mid],[left]交换，已知left左边必为0，然后mid,left右移一位
注意：因为mid碰到2直接丢右边，所以mid与left换过来的数只有可能是0，1
     当new[mid] == 0,这时说明mid,left在同一个index,所以同时右边移动
     当new[mid] == 1,这时说明mid比left快，我们把0，1按照合适的位置交换了
     此时new[left] = 0, new[mid] = 1,所以可以同时右移动
3.[mid] == 1,mid ++
4.[mid] == 2,swap(mid,right),right--.对于right换过来的数，我们还需要进一步
  检查[mid]当前的数（有可能为0,1,2)，所以mid不动，right--

讲一个发现：
例如 0 0 1 0 1
left,mid从开头遇到0就一直向前跑，直到遇到1，left就会留在1的那位上，mid还是++
这样他们交换的话就没什么问题

"""