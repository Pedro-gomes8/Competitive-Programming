class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value


class LinkedList:
    def __init__(self, nodes=None):
        self.root = None
        self.tail = None
        self.size = 0
        if nodes:
            self.add(nodes)

    def add(self, *nodes):
        for node in nodes:
            newNode = Node(node)
            self.size += 1
            if not self.root:
                self.root = newNode
                self.tail = newNode
                continue
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def pop(self):
        val = self.tail.value
        self.tail = self.tail.previous
        self.tail.next = None
        return val


test = [0, 1, 2]

a = LinkedList(test)

print(a.root.value, a.tail.value)
a.add(4)
print(a.root.value, a.tail.value)
a.pop()
print(a.root.value, a.tail.value)
