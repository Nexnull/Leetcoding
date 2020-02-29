import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        val = self.dict.pop(key)
        #这里我们首先把value给拿出来，然后再加进去一次，因为近期我们已经使用过了
        #所以要更新它的时间（在这里表现为排序）
        self.dic[key] = val
        return val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #假如说这个key在原字典有
        #说明这个是要需要更新value,所以我们先将key对应的值给pop掉
        if key in self.dic:
            self.dic.pop(key)
        #假如说这个key原字典没有
        #说明我们要把这一对加进去，然后容量要 -1
        else:
            if self.remain > 0:
                self.remain -= 1
            #假如说容量满了，那么，我们就要把字典里最后一个（停留时间最长）的pop掉
            #然后再加入新的
            else:
                self.dic.popitem(last=False)

        #所有的新key-value都是在这里加的哦
        self.dic[key] = value






"""
https://www.youtube.com/watch?v=pEmUC9Yf-CE&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=57

什么是lRU:
LRU是Least Recently Used的缩写，即最近最少使用，是一种常用的页面置换算法，选择最近最久未使用的页面予以淘汰。
 该算法赋予每个页面一个访问字段，用来记录一个页面自上次被访问以来所经历的时间t
 当须淘汰一个页面时，选择现有页面中其t 值最大的，即最近最少使用的页面予以淘汰。

这题的解法是利用双链表，hashmap来做，实现方法algocast上有
但是呢，也可以利用python自带的数据结构来做，它的存在是刚好符合这道题的
这个数据结构就是collection.OrderedDict()
它的特点它可以“维护”添加 key-value 对的顺序。简单来说，
就是先添加的 key-value 对排在前面，后添加的 key-value 对排在后面。

1.get:假如说要查的东西不在字典里，返回-1
      在字典里，那么就把它的value给pop出来，并再重新加回去一次

2.set:假如说key在字典里，那么把这个key给pop()出来
      假如不在： 内存还没满，那直接加
                内存满了，把最末尾的元素给pop掉，然后再加

"""