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
    

#using stack to verify a symbols are balanced are not
# def is_match(ch1, ch2):
#     match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#     return match_dict[ch1] == ch2


# def is_balanced(s):
#     stack = Stack()
#     for ch in s:
#         if ch=='(' or ch=='{' or ch == '[':
#             stack.push(ch)
#         if ch==')' or ch=='}' or ch == ']':
#             if stack.size()==0:
#                 return False
#             if not is_match(ch,stack.pop()):
#                 return False

#     return stack.size()==0

#using stack to reverse a string

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr   

if __name__ == '__main__':
    print(reverse_string("Onepiece is the best"))


