"""
Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not len(self.stack):
            self.min = x
            self.stack.append(x)
        elif x >= self.min:
            self.stack.append(x)
        else:
            self.stack.append((2 * x) - self.min)
            self.min = x

    def pop(self):
        """
        :rtype: None
        """
        if not len(self.stack):
            return
        top = self.stack[-1]
        if top < self.min:
            self.min = (2 * self.min) - top
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not len(self.stack):
            return
        top = self.stack[-1]
        if top < self.min:
            return self.min
        else:
            return top

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(2147483646)
    minStack.push(2147483646)
    minStack.push(2147483647)
    ex_0 = minStack.top()
    if ex_0 != 2147483647:
        print("Error")
    minStack.pop()
    ex_1 = minStack.getMin()
    if ex_1 != 2147483646:
        print("Error")
    minStack.pop()
    ex_2 = minStack.getMin()
    if ex_2 != 2147483646:
        print("Error")
    minStack.pop()
    minStack.push(2147483647)
    ex_3 = minStack.top()
    if ex_3 != 2147483647:
        print("Error")
    ex_4 = minStack.getMin()
    if ex_4 != 2147483647:
        print("Error")
    minStack.push(-2147483648)
    ex_5 = minStack.top()
    if ex_5 != -2147483648:
        print("Error")
    ex_6 = minStack.getMin()
    if ex_6 != -2147483648:
        print("Error")
    minStack.pop()
    ex_7 = minStack.getMin()
    if ex_7 != 2147483647:
        print("Error")
    pass