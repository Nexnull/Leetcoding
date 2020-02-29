from collections import defaultdict
from random import randint


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.hashmap = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.hashmap[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.hashmap[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.hashmap[val]: return False
        val_index = self.hashmap[val].pop()
        last_value = self.nums[-1]

        self.nums[val_index] = last_value
        self.hashmap[last_value].add(val_index)
        self.hashmap[last_value].discard(len(self.nums) - 1)

        self.nums.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.nums[randint(0, len(self.nums) - 1)]

"""
相对于380的改变，有重复数字
1.这就意味着，一个val,有多个对应的index,与此同时，我们还要保证它的remove是O（1），所以我们要用set作为value的数据结构
  self.hashmap[last_value].discard(len(self.nums) - 1)，在这里就体现出用set()时间复杂度上的好处了

2.其他内容基本上和380一样


"""