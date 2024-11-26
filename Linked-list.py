class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insertValues(self, arr):
        # self.head = None
        for i in arr:
            self.insertAtEnd(i)
        return

    def getLen(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def removeAt(self, index):
        if index >= self.getLen():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        return

    def insertAt(self, index, data):
        if index > self.getLen():
            raise Exception("Invalid indexes")
        if index == 0:
            self.insertAtStart(data)
        count = 0
        itr = self.head
        while itr:
            if index - 1 == count:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

    def insertAfterValue(self, data, value):
        if self.head == None:
            return
        if self.head.data == value:
            self.insertAtEnd(data)
            return
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def removeOfValue(self, value):
        if self.head == None:
            return
        if self.head.data == value:
            self.head == None
            return
        itr = self.head
        while itr:
            if itr.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next

    def print(self):
        if self.head == None:
            print("the list is empty")
            return
        toReturn = ""
        itr = self.head
        while itr:
            toReturn += itr.data + "--> "
            itr = itr.next
        print(toReturn)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtStart("Nithin S")
    ll.print()
    ll.insertAtStart("Rahul")
    ll.print()
    ll.insertAtStart("Kiran")
    ll.print()
    ll.insertAtEnd("Rudha")
    ll.print()
    ll.insertAtEnd("praveen")
    ll.print()
    ll.insertAtEnd("pavan")
    ll.print()
    ll.insertValues(["sharma", "ram", "sita", "kiran"])
    ll.print()
    ll.insertAt(1, "sunil")
    ll.print()
    ll.removeAt(1)
    ll.print()
    ll.insertAfterValue("raghu", "ram")
    ll.print()
    ll.removeOfValue("ram")
    ll.print()
    # print(ll.head)
