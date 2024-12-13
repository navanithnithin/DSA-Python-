class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def meargTwoList(self, arr1, arr2):
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                self.insertAtEnd(arr2[j])
                j += 1

            elif arr1[i] == arr2[j]:
                self.insertAtEnd(arr1[i])
                i += 1
                j += 1

            else:
                self.insertAtEnd(arr1[i])
                i += 1
        while i < len(arr1):
            self.insertAtEnd(arr1[i])
            i += 1
        while j < len(arr2):
            self.insertAtEnd(arr2[j])
            j += 1
        return self.head

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
    arr1 = [2, 4, 6, 8, 9, 10, 14, 17]
    arr2 = [3, 5, 6, 8, 11, 14, 15, 18]
    ll.print()
