class Solution:
    def __init__(self):
        self.list = []
        self.minStack = []

    def push(self, node):
        self.list.append(node)
        if not self.minStack or node < self.minStack[-1]:
            self.minStack.append(node)

    def pop(self):
        if self.list[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.list.pop()


    def top(self):
        return self.list[-1]

    def min(self):
        return self.min[-1]




if __name__ == "__main__":
    solution = Solution()


"""
找出栈中所含的最小元素，并要求时间复杂度为O（1）
就意味着你不能用任何排序算法（最快O(nlogn)) ,或者二分查找（logn)

O(1) 所能想到的数据结构就是map,但是如何利用map去查呢，真不知道 

看了答案发现，原来这题考验的是stack的改良，要求在做stack的时候同时做一个辅助
栈，用辅助栈来记录最小数

然后在pop()函数这里是有点巧妙的，因为minstack是只记录更小的数，所以当list pop
较大的数都刚好不在minstack里面，当只有pop（）到目前最小的数时，就是list[-1] == minstack[-1]的时候


"""