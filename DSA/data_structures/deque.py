from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    

pq = Queue()

pq.enqueue({
    'name': 'yaswanth',
    'dob': '20 apr, 11.01 AM',
    'rank': 120
})
pq.enqueue({
    'name': 'Anvitha',
    'timestamp': '13 july, 01.02 AM',
    'price': 132
})
pq.enqueue({
    'name': 'nancy',
    'timestamp': '25 aug, 12.03 AM',
    'price': 135
})

print(pq.size())

print(pq.dequeue())