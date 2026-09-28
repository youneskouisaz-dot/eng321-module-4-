from main import Stack, Queue, check_brackets


def test_stack():
    stack = Stack()

    assert stack.is_empty() is True

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.size() == 3
    assert stack.peek() == 30
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty() is True


def test_queue():
    queue = Queue()

    assert queue.is_empty() is True

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.size() == 3
    assert queue.peek() == 10
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    assert queue.is_empty() is True


def test_valid_brackets():
    assert check_brackets("()") is True
    assert check_brackets("[]") is True
    assert check_brackets("{}") is True
    assert check_brackets("{[()]}") is True
    assert check_brackets("(([]){})") is True


def test_invalid_brackets():
    assert check_brackets("(") is False
    assert check_brackets(")") is False
    assert check_brackets("{[}]") is False
    assert check_brackets("([)]") is False
    assert check_brackets("{{}") is False
