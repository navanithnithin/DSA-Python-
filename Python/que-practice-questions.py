import threading
import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def isEmpty(self):
        return len(self.buffer) == 0


food_order_queue = Queue()


def placeOrder(orders):
    for order in orders:
        print("Placing order for: {}".format(order))
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serveOrders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving : {}".format(order))
        time.sleep(2)


if __name__ == "__main__":
    orders = ["biryani", "burger", "pasta", "sumosa", "pizza","idly"]
    t1 = threading.Thread(target=placeOrder, args=(orders,))
    t2 = threading.Thread(target=serveOrders)
    t1.start()
    t2.start()
