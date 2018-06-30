class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def remove(self,val):
        current = self.head
        previous = None
        while current != None:
            if current.value == val:
                if previous != None:
                    previous.next = current.next
                    if current.next == None:
                        previous = self.tail
                else:
                    self.head = self.head.next
                if self.head == None:
                    self.nail = None
                return True
            previous = current
            current = current.next
        return False

    def remove_all(self,val):
        current = self.head
        previous = None
        while current != None:
            if current.value == val:
                if previous != None:
                    previous.next = current.next
                    current = previous
                    if current.next == None:
                        previous = self.tail
                else:
                    self.head = self.head.next
                if self.head == None:
                    self.nail = None
            previous = current
            current = current.next

    def search(self,val):
        current = self.head
        list = []
        while current != None:
            if current.value == val:
                list.append(current)
            current = current.next
        return print(list)

    def clear(self):
        self.__init__()

    def sum_all(self):
        node = self.head
        sum = 0
        while node != None:
            sum += 1
            node = node.next
        return sum

    def insert(self, item, item_after):
        current = self.head
        while current != None:
            if current.value == item_after.value:
                item.next = current.next
                current.next = item
            current = current.next



def compare(list_one, list_two):
    count_one = 0
    count_two = 0
    current_one = list_one.head
    current_two = list_two.head
    while current_one != None:
        count_one += 1
        current_one = current_one.next
    while current_two != None:
        count_two += 1
        current_two = current_two.next
    if count_one == count_two:
        ss_list = LinkedList()
        current_one = list_one.head
        current_two = list_two.head
        while current_one != None and current_two != None:
            ss_list.add_in_tail(Node(current_one.value + current_two.value))
            current_one = current_one.next
            current_two = current_two.next
        return ss_list.print_all_nodes()





