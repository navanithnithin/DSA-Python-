class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.getHash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key: 
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.getHash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return self.arr[h]

    def __delitem__(self, key):
        h = self.getHash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print("del", index)
                del self.arr[h][index]


ht = HashTable()

ht.getHash("march 6")
ht.getHash("march 17")
print(ht.getHash("march 6"))
print(ht.getHash("march 17"))
# ht.add("month", 11)
ht["june 12"] = 2000
ht["march 6"] = 100
# ht["march 6"] = 500
ht["march 17"] = 3000
print(ht.arr)
print(ht["march 6"])
print(ht["march 17"])
del ht["march 17"]
print(ht.arr)
