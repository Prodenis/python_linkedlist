class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# 4
def brackets(str):
    stack = Stack()
    counter = 0
    for i in range(len(str)):
        stack.push(str[i])
    while stack.size() > 0:
        if stack.pop() == "(":
            counter += 1
        if stack.pop() == ")":
            counter -= 1
    if counter > 0:
        return False
    else:
        return True

# 1
class Stack2:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        return self.stack.insert(0, value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]

    def size(self):
        return len(self.stack)

# 5
def postfix(str):
    stack = Stack()
    stack2 = Stack()
    for i in reversed(range(len(str))):
        stack.push(str[i])
    while stack.size() > 0:
        if stack.peak().isdigit():
            stack2.push(stack.pop())
        if stack.peak() == "+":
            stack.pop()
            stack2.push(int(stack2.pop()) + int(stack2.pop()))
        if stack.peak() == "*":
            stack.pop()
            stack2.push(int(stack2.pop()) * int(stack2.pop()))
        if stack.peak() == "-":
            stack.pop()
            stack2.push(int(stack2.pop()) - int(stack2.pop()))
        if stack.peak() == "=":
            stack.pop()
            return stack2


