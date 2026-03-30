class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumTracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minimumTracker) == 0:
            self.minimumTracker.append(val)
        else:
            self.minimumTracker.append(min(self.minimumTracker[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minimumTracker.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimumTracker[-1]
