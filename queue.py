class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def rotation(n, queue):
    for i in range(n):
        queue.enqueue(queue.dequeue())
    return queue


class QueueStack:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.count = 0

    def enqueue(self, item):
        self.list1.append(item)
        self.count += 1

    def dequeue(self):
        if self.list1.__len__() == 0:
            return
        while self.count > 0:
            self.count -= 1
            self.list2.append(self.list1.pop())
        return self.list2.pop()









