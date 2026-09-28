class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def check_brackets(text):
    stack = Stack()

    opening = "([{"
    closing = ")]}"

    matches = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        if char in opening:
            stack.push(char)

        elif char in closing:
            if stack.is_empty():
                return False

            top = stack.pop()

            if top != matches[char]:
                return False

    return stack.is_empty()


def check_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    return check_brackets(content)


if __name__ == "__main__":
    print("Stack Test")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top:", stack.peek())
    print("Pop:", stack.pop())
    print("Size:", stack.size())

    print()

    print("Queue Test")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Front:", queue.peek())
    print("Dequeue:", queue.dequeue())
    print("Size:", queue.size())

    print()

    print("Bracket Checker Test")

    valid_code = "{ [ ( ) ] }"
    invalid_code = "{ [ ( ] ) }"

    print(valid_code, "->", check_brackets(valid_code))
    print(invalid_code, "->", check_brackets(invalid_code))
