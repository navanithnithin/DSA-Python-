class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        if self.head == None:
            self.head = Node(data, self.head, None)
            return
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insertAt(self, index, data):
        if index > self.getLength:
            raise Exception("invalid index")
        if index == 0:
            self.insertAtStart(data)
        itr = self.head
        count = 0
        while itr:
            if index == count - 1:
                itr.next = Node(data, itr.next, itr)
                break
            count += 1
            itr = itr.next

    def removeAt(self, index):
        if index > self.getLength():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                return
            count += 1
            itr = itr.next

    def printForward(self):
        dlString = ""
        itr = self.head
        while itr:
            dlString += itr.data + " -->"

            itr = itr.next
        print(dlString)

    def getLastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def printBackward(self):
        if self.head == None:
            print("Empty list")
            return
        dlString = ""
        itr = self.getLastNode()
        while itr:
            dlString += itr.data + " <-- "
            itr = itr.prev
        print(dlString)


if __name__ == "__main__":
    dl = DoubleLinkedList()
    dl.insertAtStart("Nithin S")
    dl.printForward()
    dl.insertAtStart("Rahul")
    dl.printForward()
    dl.insertAtStart("Kiran")
    dl.printForward()
    dl.insertAtEnd("Rudha")
    dl.printForward()
    dl.insertAtEnd("praveen")
    dl.printForward()
    dl.insertAtEnd("pavan")
    dl.printForward()
    dl.printBackward()
    # dl.printForward()
    dl.removeAt(1)
    dl.printBackward()
    
    # dl.printForward()

    
    
