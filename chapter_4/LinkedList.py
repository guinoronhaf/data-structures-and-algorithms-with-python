class Node: # classe que representa o nó

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList: # classe que representa a Linked List

    def __init__(self):
        self.head = None # cabeça (início)
        self.tail = None # cauda (final)
        self.size = 0 # tamanho (comprimento)

    def is_empty(self):
        return self.head is None

    def addFirst(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def add(self, index, data):
        if index < 0 or index >= self.size:
            print("Invalid index to insert.")
        elif index == 0:
            self.addFirst(data)
        else:
            prev = None
            current = self.head
            idx = 0
            while idx < index:
                prev = current
                current = current.next
                idx += 1
            new_node = Node(data)
            prev.next = new_node
            new_node.next = current
            self.size += 1

    def index_of(self, data):
        current = self.head
        idx = 0
        while current is not None:
            if current.data == data:
                return idx
            current = current.next
            idx += 1
        return -1

    def contains(self, data):
        return self.index_of(data) != -1

    def removeFirst(self):
        if self.head is None:
            print("No such element to remove!")
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def removeLast(self):
        if self.head is None:
            print("No such element to remove!")
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            prev = None
            current = self.head
            while current.next is not None:
                prev = current
                current = current.next
            prev.next = None
            self.tail = prev
        self.size -= 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            print("No such element to remove at that index!")
        elif index == 0:
            self.removeFirst()
        elif index == self.size - 1:
            self.removeLast()
        else:
            prev = None
            current = self.head
            idx = 0
            while idx < index:
                prev = current
                current = current.next
                idx += 1
            prev.next = current.next
            self.size -= 1

    def iter(self):
        current = self.head
        while current is not None:
            data = current.data
            current = current.next
            yield data
