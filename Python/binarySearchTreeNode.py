class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inOrderTraversel(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversel()
        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversel()
        return elements

    def postOrderTraversel(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversel()

        if self.right:
            elements += self.right.inOrderTraversel()
        elements.append(self.data)
        return elements

    def preOrderTraversel(self):
        elements = [self.data]
        if self.left:
            elements += self.left.inOrderTraversel()

        if self.right:
            elements += self.right.inOrderTraversel()
        return elements
    def findMax(self):
        if self.right ==None:
            return self.data
        else:
            return self.right.findMax()
    def findMin(self):
        if self.left == None:
            return self.data
        return self.left.findMin()

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def sumOf(self):
        sum=0
        for i in self.inOrderTraversel():
            sum+=i
        return sum


def builtTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(len(elements)):
        root.addChild(elements[i])
    return root


if __name__ == "__main__":

    number = [17, 99, 100, 56, 4, 1,0, 20, 9, 23, 18, 34]
    numberTree = builtTree(number)

    print(numberTree.inOrderTraversel())
    print(numberTree.data)
    print(numberTree.postOrderTraversel())
    print(numberTree.data)
    print(numberTree.preOrderTraversel())
    print(numberTree.data)
    print(numberTree.search(220))
    print(numberTree.findMax())
    print(numberTree.findMin())
    print(numberTree.sumOf())
