class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def __setitem__(self, key, value):
        h = self.getHash(key)

        if self.arr[h] == None:
            self.arr[h] = (key, value)
        else:
            newHash = self.getSlots(key, h)
            self.arr[newHash] = (key, value)

    def __getitem__(self, key):
        h = self.getHash(key)
        if self.arr[h] == None:
            return
        probRange = self.getProb(h)
        for probIndex in probRange:
            element = self.arr[probIndex]
            if element == None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.getHash(key)
        if self.arr[h] == None:
            return
        probRange = self.getProb(h)
        for probIndex in probRange:
            element = self.arr[probIndex]
            if element == None:
                return
            if element[0] == key:
                element = None
                return

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def getProb(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def getSlots(self, key, index):
        probRange = self.getProb(index)
        for i in probRange:
            if self.arr[i] == None:
                return i
            if self.arr[i][0] == key:
                return i
        raise Exception("Hash map is filled")


if __name__ == "__main__":
    h = HashTable()
    ht = HashTable()
    ht["march 6"] = 2000
    ht["march 17"] = 3000
    ht["march 7"] = 9000
    # del ht["march 7"]
    print(ht.arr)
    print(ht["march 7"])
