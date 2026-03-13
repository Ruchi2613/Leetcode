class SpecialStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int):
        self.stack1.append(val)
        if not self.stack2 or self.stack2[-1] >= val:
            self.stack2.append(val)

    def pop(self):
        if not self.stack1:
            return None

        val = self.stack1.pop()
        if self.stack2 and self.stack2[-1] == val:
            self.stack2.pop()

    def top(self):
        if not self.stack1:
            return None
        return self.stack1[-1]

    def getMin(self):
        if not self.stack2:
            return None
        return self.stack2[-1]

    def isEmpty(self):
        return len(self.stack1) == 0


if __name__ == "__main__":
    stack = SpecialStack()

    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.push(2)
    stack.push(8)
    stack.push(1)

    print("Top:", stack.top())        # Output: 1
    print("Min:", stack.getMin())     # Output: 1

    stack.pop()  # Removes 1
    print("Top after pop:", stack.top())  # Output: 8
    print("Min after pop:", stack.getMin())  # Output: 2

    stack.pop()  # Removes 8
    stack.pop()  # Removes 2
    print("Top after 3 pops:", stack.top())  # Output: 7
    print("Min after 3 pops:", stack.getMin())  # Output: 3

    stack.push(0)
    print("Top after pushing 0:", stack.top())  # Output: 0
    print("Min after pushing 0:", stack.getMin())  # Output: 0

    # Emptying the stack
    while not stack.isEmpty():
        print(f"Popped: {stack.top()}, Min: {stack.getMin()}")
        stack.pop()

    print("Is stack empty?", stack.isEmpty())