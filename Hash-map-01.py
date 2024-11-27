class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __getitem__(self, key):
        h = self.getHash(key)
        for i in self.arr[h]:
            if i[0] == key:
                return i[1]
        return self.arr[h]

    def __delitem__(self, key):
        h = self.getHash(key)
        for i, val in enumerate(self.arr[h]):
            if val[0] == key:
                print("del", i)
                del self.arr[h][i]

    def __setitem__(self, key, value):
        found = False
        h = self.getHash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))


if __name__ == "__main__":
    h = HashTable()
    h["march 6"] = 1000
    h["march 17"] = 1000
    h.getHash("march 6")
