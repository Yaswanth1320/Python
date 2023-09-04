#Stack implementation with python with dequeue

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.peek()
s.is_empty()
s.size()


