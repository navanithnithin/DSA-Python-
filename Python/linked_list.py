class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def remove_at(self, index):
        if index < 0 or index >= self.getLength():
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

    def insert_values(self, arr_list):
        self.head = None
        for val in arr_list:
            self.insert_at_end(val)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index >= self.getLength() or index < 0:
            raise Exception("invalid index")
        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:

            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insertAfterValue(self, data_after, data):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.insert_at_end(data)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next

    def removeByValue(self, value):
        if self.head == None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            # print(itr.data)
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print("empty linked list")
            return

        itr = self.head
        # print(self.head)
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.print()  
    ll.insert_at_begining(47)
    ll.print()
    ll.insert_at_begining(97)
    ll.print()
    ll.insert_at_end(69)
    # ll.print()
    ll.insert_values(["nithin", "ram", "sita", "kiran"])
    ll.print()
    ll.remove_at(1)
    ll.print()
    ll.insert_at(2, "rahul")
    ll.print()
    ll.insert_at(2, "pranith")
    ll.print()
    ll.insert_at(0, "karan")
    ll.print()
    ll.insert_at_end("madhu")
    ll.print()
    ll.removeByValue("rahul")
    ll.print()
    ll.insertAfterValue("kiran", "pandu")
    ll.print()
