class Node2:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def test_list(self):
        current = self.head
        list = []
        while current != None:
            list.append(current.value)
            current = current.next
        return list

    # 2.3
    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            item.next = None
            item.prev = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

    # 2.2
    def insert(self, node, node_before):
        current = self.head
        while current != None:
            if current.value == node_before.value:
                node.prev = current
                current.next = node
                node.next = current.next.prev
                current.next.prev = node
                return True
            current = current.next

    # 2.1
    def remove(self, val):
        current = self.head
        previous = None
        while current != None:
            if current.value == val:
                if previous != None:
                    previous.next = current.next
                    if current.next == None:
                        previous = self.tail
                    else:
                        current.next.prev = previous
                else:
                    self.head = self.head.next
                return True
            previous = current
            current = current.next
        return False



n1 = Node2(12)
n2 = Node2(55)
n1.next = n2
n2.prev = n1

s_list = LinkedList2()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_head(Node2(20))
s_list.add_in_tail(Node2(40))
#s_list.add_in_head(Node2(50))
s_list.insert(Node2(24), Node2(20))
#s_list.remove(12)
s_list.print_all_nodes()
