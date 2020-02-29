"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty

"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2.pop(-1)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
            return self.stack2.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        查看队列最后一个元素(最晚出去的元素)
        """
        if self.stack1:
            return self.stack1[0]
        else:
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0

"""
和剑指offer的第五题一样
"""