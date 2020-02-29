"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
类型：stack & queue
"""

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop(-1)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
            return self.stack2.pop(-1)


"""
remark:
pop() = pop(-1)

原理：
queue为先进先出
stack为先进后出
这里我们用stack1来接受push的node
stack2的元素，都是来源与stack1.pop(-1)
因为stack1.pop(-1),后进来的元素，把这些元素append进stack2,使得这些后进的元素反而压了箱底
这时在stack2.pop(-1),使得先进的元素pop出去了

stack2: []
stack1: [1,2,3,4]
pop(-1)
stack2: [4,3,2,1]
出来的元素为 1

答案：
1.init里面建两个stack
2.push就直接push进stack1
3.pop时，如果有stack2有元素，直接pop(-1)。如果没有，则先吧stack1的元素一个个pop出来
append进stack2,然后再return stack2.pop(-1)


"""