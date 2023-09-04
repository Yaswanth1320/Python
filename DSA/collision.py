#Collision control using chaining

class HashTable:  
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.max
    
    def __getitem__(self, key):
        index = self.get_hash(key)
        for i in self.arr[index]:
            if i[0] == key:
                return i[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]


table = HashTable()
table["day 6"] = 310
table["day 7"] = 420
table["day 8"] = 67
table["day 17"] = 63457
print(table.arr)
print(table["day 17"])