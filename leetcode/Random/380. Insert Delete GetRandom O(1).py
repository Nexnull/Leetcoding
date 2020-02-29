"""
380. Insert Delete GetRandom O(1)
使这三个方法的时间复杂度都是O(1)
"""
from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            self.nums.append(val)
            self.hashmap[val] = len(self.nums)-1
            return True

        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            val_index = self.hashmap[val]
            last_value = self.nums[-1]

            # 把last_value的index变成 原来val所在的index
            # 把last_value 放在val之前所在的index上(在self.nums里已经把val抹除了)
            # 所做的一切，都是把last_value,放在val本应该存在的位置上，然后我们再把val给去除

            self.hashmap[last_value],self.nums[val_index] = val_index,last_value

            # 把多余的last_value 给pop()掉，因为它已经附值在val之前的index上了
            # 把hashmap 中把 val给去掉
            self.nums.pop(),self.hashmap.pop(val,0)
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[randint(0,len(self.nums)-1)]

"""
https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
答案：
1.这题就看出来了两种数据结构了
2. list,查找是n,pop,append是1， hashmap,查找,pop,append都是O（1）
3. 所以在insert和remove里，我们要看val在不在数据结构以内，我们要用hashmap来查找
因为是O（1），而not in list的话，时间复杂度是O(n)

4.remove 这个函数的处理方法有点巧妙， 我们得先把val 的index , 和nums[-1] 的val找出来
    把val放在nums的位置上，同时把val在字典中的位置换成num[-1]
    然后再pop（）
"""