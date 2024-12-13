class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnding(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insertValues(self, array):
        for val in array:
            self.insertAtEnding(val)

    def removeAt(self, index):
        if index > self.getLength() or index < 0:
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

    def insertAt(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid index")
        if index == 0:
            self.insertAtBegining(data)
        count = 0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=Node(data,itr.next)
                break
            itr=itr.next
            count+=1

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBegining("Nithin S")
    ll.insertAtBegining("Kiran")
    ll.insertAtEnding("Murmu")
    ll.removeAt(2)
    ll.print()
    print(ll.getLength())
    ll.insertValues(["ravi", "virat", "guru"])
    ll.insertAt(4,"raghu")
    ll.print()
