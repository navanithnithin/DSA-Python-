from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0

    def front(self):
        return self.buffer[-1]


def produce_binary_number(num):
    number = Queue()
    number.enqueue("1")
    for i in range(num):
        front = number.front()
        print("  ", front)
        number.enqueue(front + "0")
        number.enqueue(front + "1")
        number.dequeue()


if __name__ == "__main__":
    produce_binary_number(100)
