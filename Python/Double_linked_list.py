class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None, itr)

    def printForward(self):
        if self.head == None:
            print("Linked list is empty")
            return
        dllstr = ""
        itr = self.head
        while itr:
            dllstr += str(itr.data) + "-->"
            itr = itr.next

        return dllstr

    def insertAt(self, index, data):
        if index > self.getLength() or index < 0:
            raise Exception("invalid INdex")
        if index == 0:
            self.insertAtBegining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next, itr)
                break
            itr = itr.next
            count += 1

    def removeAt(self, index):
        if index > self.getLength() or index < 0:
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            count += 1
            itr = itr.next

    def printBackward(self):
        if self.head == None:
            print("Linked list is empty")
            return
        lastNode = self.getLastNode()
        itr = lastNode
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + "-->"
            itr = itr.prev

        return dllstr

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def getLastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insertAtBegining("ram")
    dll.insertAtBegining("sita")
    dll.insertAtEnd("Pawan")
    dll.insertAtEnd("ragavandra")
    print(dll.printBackward())
    print(dll.printForward())
    dll.insertAt(2, "praveen")
    dll.removeAt(2)
    print(dll.printForward())
