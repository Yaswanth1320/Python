#Hashtable implememtation in python

class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h%self.max
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    

table = HashTable()
table["yaswanth"] = 90
table["nikitha"] = 92
table["sadwika"] = 97
table["sunil"] = 91
table["harshitha"] = 95
print(table["yaswanth"]) #Before removing
del table["yaswanth"]
print(table["yaswanth"]) #After removing

