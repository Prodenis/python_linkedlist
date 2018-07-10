class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0,item)

    def removeFront(self):
        return self.queue.pop()

    def removeTail(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


def palindrome(str):
    qu = Deque()
    for i in range(len(str)):
        qu.addFront(str[i])
    for i in range(len(str)):
        if qu.removeFront() != str[i]:
            return False
    return True


