class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def getHashKey(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max

    def __getitem__(self, key):
        h = self.getHashKey(key)
        if self.arr[h] == None:
            return
        probRange = self.getProb(h)
        for probIndex in probRange:
            element = self.arr[probIndex]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.getHashKey(key)
        if self.arr[h] == None:
            self.arr[h] = (key, value)
        else:
            newHash = self.getSlot(key, h)
            self.arr[newHash] = (key, value)
        print(self.arr)

    def getProb(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def getSlot(self, key, index):
        probRange = self.getProb(index)
        for probIndex in probRange:
            if self.arr[probIndex] is None:
                return probIndex
            if self.arr[probIndex][0] == key:
                return probIndex

        raise Exception("Hash Table is full")

    def __delitem__(self, key):
        h = self.getHashKey(key)
        probRange = self.getProb(h)
        for probIndex in probRange:
            if self.arr[probIndex] == None:
                return
            if self.arr[probIndex][0] == key:
                self.arr[probIndex] = None
        print(self.arr)


if __name__ == "__main__":
    ht = HashTable()
    ht["march 6"] = 2000
    ht["march 17"] = 3000
    ht["march 7"] = 9000
    del ht["march 7"]
    print(ht["march 7"])
