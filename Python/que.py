# que=[]
# que.insert(0,9)
# que.insert(0,5)
# que.insert(0,10)
# print(que)
# print(que.pop()) #first in first out

from collections import deque

# q= deque()
# q.appendleft(19)
# q.appendleft(34)
# q.appendleft(76)
# q.appendleft(28)
# print(q)
# print(q.pop())
# print(q)


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == "__main__":
    dq = Queue()
    dq.enqueue("nithin")
    dq.enqueue("ram")
    dq.enqueue("sita")
    dq.enqueue("praveen")
    print(dq.buffer)
    print(dq.dequeue())
    print(dq.buffer)
