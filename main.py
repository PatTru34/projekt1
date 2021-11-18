from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any, next: 'Node'):
        self.value = value
        self.next = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head, tail) -> None:
        self.head = head
        self.tail = tail

    def __len__(self):
        x = self.head
        wynik = 0
        while x is not None:
            wynik = wynik + 1
            x = x.next
        return wynik

    def __str__(self) -> str:
        wynik = ""
        x = self.head
        while x is not None:
            if x.next is not None:
                wynik += str(x.value) + " -> "
            else:
                wynik += str(x.value)
            x = x.next
        return wynik

    def push(self, value: Any) -> None:
        if self.head == None:
            self.head = Node(value, None)
            self.tail = self.head
        else:
            x = self.head
            self.head = Node(value, x)

    def append(self, value: Any) -> None:
        if self.tail == None:
            self.tail = Node(value, None)
            self.head = self.tail

        else:
            x = self.head
            while x is not None:
                if x.next is None:
                    x.next = Node(value, None)
                    self.tail = x.next
                    x = None
                else:
                    x = x.next

    def node(self, at: int) -> Node:
        x = self.head
        i = 0
        while x is not None:
            if i == at:
                return x
            i = i + 1
            x = x.next

    def insert(self, value: Any, after: Node) -> None:
        x = self.head

        while x is not None:
            if x == after:
                y = x.next
                x.next = Node(value, y)
                x = None
            else:
                x = x.next

    def pop(self) -> Any:
        x = self.head
        self.head = x.next
        return x.value

    def remove_last(self) -> Any:
        x = self.head
        y = self.head

        while x is not None:
            if x.next is None:
                wynik = x
                y.next = None
                self.tail = y
                x = None
                return wynik.value
            else:
                y = x
                x = x.next

    def remove(self, after: Node) -> Any:
        x = self.head

        while x is not None:
            if x == after:
                x.next = x.next.next
                x = None
            else:
                x = x.next


class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList(None, None)

    def __len__(self):
        return len(self._storage)

    def __str__(self) -> str:
        wynik = ""
        x = self._storage.head
        while x is not None:
            wynik += str(x.value) + "\n"

            x = x.next
        return wynik

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList(None, None)

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        wynik = ""
        x = self._storage.head
        while x is not None:
            if x.next is not None:
                wynik += str(x.value) + ", "
            else:
                wynik += str(x.value)

            x = x.next
        return wynik

    def enqueue(self, element) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def peek(self) -> Any:
        return self._storage.tail


list_: LinkedList = LinkedList(head=None, tail=None)
assert list_.head == None
list_.push(1)
list_.push(0)
print(list_)
assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

# print(list_)
# print(list_.node(at=0).value)
# print(str(list_.pop()) + "\n")
# print(list_)
# print(str(list_.remove_last().value)+"\n")
# print(str(list_)+"\n")
# list_.remove(list_.node(at=0))
# print(list_)
# print(len(list_))


stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
print(stack)

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue)
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
