class MinStack():
    def __init__(self):
        self.stack = []
        self.minStack = []

    def pop(self):
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        return self.stack.pop()

    def peak(self):
        if not self.stack :
            return None
        return self.stack[-1]

    def push(self, num):
        if not self.stack:
            top = None
        else:
            top = self.stack[-1]

        self.stack.append(num)
        if top is None or num < top:
            self.minStack.append(num)

    def min(self):
        if not self.minStack:
            while not self.stack:
                self.minStack.append(self.stack.pop())
        return self.minStack[-1]

    def printStack(self):
        print(self.stack)


def main():
    stack = MinStack()
    stack.push(8)
    print(stack.min())
    stack.push(4)
    print(stack.min())
    stack.push(10)
    print(stack.min())


main()
