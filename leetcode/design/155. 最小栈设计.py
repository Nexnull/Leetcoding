class MinStack(object):

    #mini是一个辅助栈，与data同增同减，但是mini添加的时候
    #是添加当前（栈自身，以及新增元素）的最小值
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mini = []
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.mini) == 0 or x < self.mini[-1]:
            self.mini.append(x)
        else:
            self.mini.append(self.mini[-1])


    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.mini.pop(-1)
            return self.data.pop(-1)


    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.mini:
            return self.mini[-1]