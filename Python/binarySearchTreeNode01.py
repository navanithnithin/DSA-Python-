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

    def inOrderTraversal(self):
        element = []
        if self.left:
            element += self.left.inOrderTraversal()
        element.append(self.data)
        if self.right:
            element += self.right.inOrderTraversal()
        return element

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False


def builtTree(element):
    root = BinarySearchTreeNode(element[0])
    for i in range(len(element)):
        root.addChild(element[i])
    return root


if __name__ == "__main__":
    number = [17, 99, 100, 56, 4, 1, 20, 9, 23, 18, 34]
    numberTree = builtTree(number)

    print(numberTree.inOrderTraversal())
    print(numberTree.search(220))
