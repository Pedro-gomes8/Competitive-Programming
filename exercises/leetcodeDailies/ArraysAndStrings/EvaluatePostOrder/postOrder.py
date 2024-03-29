class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class Stack:
    def __init__(self, args=None):
        if args:
            self.length = len(args)
            for i in range(len(args)):
                if i == 0:
                    node = Node(args[i])
                    self.first = node
                    self.last = node
                else:
                    self.add(args[i])
        else:
            self.first = None
            self.last = None
            self.length = 0

    def add(self, element):
        newNode = Node(element)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            newNode.prev = self.last
            self.last = newNode
        self.length += 1

    def remove(self):
        if self.length >= 1:
            tmp = self.last.value
            if self.length > 1:
                self.last = self.last.prev
                self.last.next = None
            self.length -= 1
        return int(tmp)


def evalRPN(tokens: list[str]) -> int:
    stack = Stack()
    for char in tokens:
        if char == "+":
            operand1 = stack.remove()
            operand2 = stack.remove()
            stack.add(operand2 + operand1)
        elif char == "-":
            operand1 = stack.remove()
            operand2 = stack.remove()
            stack.add(operand2 - operand1)
        elif char == "*":
            operand1 = stack.remove()
            operand2 = stack.remove()
            stack.add(operand2 * operand1)
        elif char == "/":
            operand1 = stack.remove()
            operand2 = stack.remove()
            stack.add(int(operand2 / operand1))
        else:
            stack.add(char)

    return stack.last.value


print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
