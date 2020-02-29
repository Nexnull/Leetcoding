"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)



    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue1 < 0:
            return None
        if len(self.queue1) == 1:
            return self.queue1.pop(0)
        else:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            pop_element = self.queue1.pop(0)
            while self.queue2:
                self.queue1.append(self.queue2.pop(0))
            return pop_element



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return  len(self.queue1) == 0 and len(self.queue2) == 0

"""
用两个队列实现一个栈的功能?要求给出算法和思路!

入栈：将元素进队列A

出栈：
    1.判断队列A中元素的个数是否为1，如果等于1，则出队列
     2.否则将队列A中的元素,以此出队列并放入队列B，直到队列A中的元素留下一个，
     然后队列A出队列，再把队列B中的元素出队列以此放入队列A中。
     
     
     入队：将元素进栈A

出队：判断栈B是否为空，如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈；

 如果不为空，栈B直接出栈。
"""