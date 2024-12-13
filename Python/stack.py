from collections import deque

# stack = deque()
# print(dir(stack))
# stack.append("1")
# stack.append("2")
# stack.append("3")
# stack.append("4")
# stack.append("5")
# stack.append("6")
# stack.append("7")
# print(stack)
# stack.pop()
# print(stack)


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == "__main__":
    s = Stack()
    s.push(9)
    s.push(90)
    s.push(25)
    s.push(89)
    print(s.pop())
    print(s.size())
