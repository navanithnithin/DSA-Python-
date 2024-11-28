from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return self.container == None

    def size(self):
        return len(self.container)

    def reverse(self, string):
        self.string = deque()
        newStr = ""
        for i in string:
            self.string.append(i)
        for i in range(len(self.string)):
            newStr += self.string.pop()
        return newStr

    def isMatch(self, c1, c2):
        dict1 = {")": "(", "]": "[", "}": "{"}
        return dict1[c1] == c2

    def blanced(self, string):
        self.newstr = deque()
        for i in string:
            if i == "(" or i == "[" or i == "{":
                self.newstr.append(i)
            if i == ")" or i == "]" or i == "}":
                if len(self.newstr) == 0:
                    return False
                if not self.isMatch(i, self.newstr.pop()):
                    return False
        return len(self.newstr) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(90)
    s.push(25)
    s.push(89)
    print(s.pop())
    print(s.size())
    print(s.reverse("Rama"))
