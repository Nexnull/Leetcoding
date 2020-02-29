import sys


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return False

        min1 = sys.maxsize
        min2 = sys.maxsize

        for num in nums:
            if num > min2:
                return True
            elif num > min1 and num < min2:
                min2 = num
            elif num < min1:
                min1 = num

        return False

"""
Time:O(n) Space:O(1)
https://www.youtube.com/watch?v=xV_AS08-OeA
答案：
这里能优化的地方在于，总共有3个case
我们用 min1来储存序列中最小的元素，min2来储存序列中第二小的元素，所以会衍生出以下三种情况

        min1       min2
    ^          ^             ^
    |          |             |

    case1      case2        case3    
 num < min1   min1<num<min2  num > min2
 更新min1       更新min2       return True

"""