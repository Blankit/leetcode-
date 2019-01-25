# coding:utf-8
'''
参考
1. 用数组实现栈
2. 在初始化时，建立两个栈stack与min_stack.
3. stack用于常规的push、pop、top.min_stack用于取最小值
4. 每次在stack压入一个数据的时候，在min_stack中也需压入一个数据。
5. minstack在压入数据时有条件：如果待压入的数据比min_stack小，则将这个数压入min_stack,否则，压入当前min_stack的栈顶的数据
6. 在弹出时，min_stack也许弹出
'''


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack:#如果待压入的数据比min_stack小，则将这个数压入min_stack，否则，压入当前min_stack的栈顶的数据
            if self.min_stack[-1] >= x:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)

        return

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]