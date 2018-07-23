class Node2:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class OrderedList:
    def __init__(self, keep):
        self.head = None
        self.tail = None
        self.keep = keep

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            print(node.prev)
            node = node.next

    def compare(self, item, item2):
        if self.keep == "ascending":
            if item >= item2:
                return item
            else:
                return item2
        if self.keep == "descending":
            if item >= item2:
                return item2
            else:
                return item

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if self.compare(item, current.value) == current.value:
                print(previous)
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node2(item)
        if previous is None:
            if self.head is None:
                self.head = item
                temp.next = None
                temp.prev = None
            else:
                self.head.prev = temp
                temp.next = self.head
            self.head = temp
            # temp.next = self.head
            # self.head = temp
        else:
            old_current_next = current.next
            temp.prev = current
            current.next = temp
            temp.next = old_current_next
            current.next.prev = temp


s_list = OrderedList("descending")
s_list.add(20)
s_list.add(21)
s_list.add(100)
s_list.add(78)
s_list.add(79)
s_list.add(120)
s_list.add(23)
s_list.print_all_nodes()