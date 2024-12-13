from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]

    def isMatch(self, ch1, ch2):
        dict1 = {")": "(", "]": "[", "}": "{"}
        return dict1[ch1] == ch2

    def reverse(self, string):
        self.newStack = deque()
        newStr = ""

        for i in string:
            self.newStack.append(i)
        for i in range(len(self.newStack)):
            newStr += self.newStack.pop()
        return newStr

    def isBalanced(self, str1):
        self.s1 = deque()
        for i in str1:
            if i == "(" or i == "{" or i == "[":
                self.s1.append(i)
            if i == ")" or i == "}" or i == "]":
                if len(self.s1) == 0:
                    return False
                if not self.isMatch(i, self.s1.pop()):
                    return False
        return len(self.s1) == 0


if __name__ == "__main__":
    s = Stack()
    print(s.reverse("This is Nithin S from MapSystems"))
    print(s.isBalanced("((a+b))"))
