class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, data: int) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self) -> bool:
        return self.front is None

    def add_front(self, data: int) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, data: int) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return data

    def remove_rear(self):
        if self.is_empty():
            return None
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return data

def input_queue(queue_list):
    queue = Queue()
    for item in queue_list.split():
        queue.enqueue(item)

    print("Queue:")
    while not queue.is_empty():
        print(queue.dequeue())

def input_dequeue(queue_list):
    deque = Deque()
    for item in queue_list.split():
        deque.add_front(item)

    print("Deque from front:")
    while not deque.is_empty():
        print(deque.remove_front())