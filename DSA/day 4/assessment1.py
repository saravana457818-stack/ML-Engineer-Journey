class Queue:
    def __init__(self):
        self.queue = []


    def enqueue(self, item):
        self.queue.append(item)
        return f"{item} inserted"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

 
    def rear(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[-1]


    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    
    def display(self):
        return self.queue
q = Queue()

print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))

print("Queue:", q.display())
print("Front:", q.peek())
print("Rear:", q.rear())

print("Dequeued:", q.dequeue())

print("Queue after dequeue:", q.display())
print("Size:", q.size())
print("Is Empty:", q.is_empty())