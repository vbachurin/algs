class MinStack(object):

    stack = []
    pos = -1

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.pos = -1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.pos += 1
        if self.pos >= len(self.stack):
            self.stack.append(x)
        else:
            self.stack[self.pos] = x
        

    def pop(self):
        """
        :rtype: None
        """
        self.pos = max(self.pos - 1, -1)
        if self.pos == -1: self.stack = []
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.pos] if self.stack else None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.pos < 0: return None
        return min(self.stack[:self.pos+1]) if self.pos > 0 else self.stack[0]

obj = MinStack()
# obj.push(-2)
# obj.push(0)
obj.push(-5)
obj.push(4)
obj.pop()
obj.push(3)
obj.push(3)
obj.push(3)
obj.pop()
obj.pop()
obj.push(-6)
# obj.pop()
# print(obj.top())
print(obj.getMin())