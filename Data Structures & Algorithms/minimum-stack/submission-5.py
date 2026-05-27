class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        copy = self.stack[:]
        minimum = copy.pop()
        while copy:
            curr = copy.pop()
            if curr < minimum:
                minimum = curr
        return minimum
