# Queue in Data Structures (DSA)

## What is a Queue?
A **Queue** is a linear data structure that follows **FIFO (First In, First Out)**.

- Insert at **Rear**
- Delete from **Front**

## Operations
- Enqueue
- Dequeue
- Peek
- Rear
- is_empty()
- size()

## Example

Initial:
```
[]
```

Enqueue 10,20,30:
```
Front        Rear
10 -> 20 -> 30
```

Dequeue:
Removes **10**

Queue becomes:
```
20 -> 30
```

## Python Implementation

```python
class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue
```

## Deque
A **Deque (Double Ended Queue)** allows insertion and deletion from both ends.

```python
from collections import deque

dq=deque()
dq.append(20)
dq.appendleft(10)
dq.append(30)

print(dq)

dq.pop()
dq.popleft()
```

## Queue vs Stack

| Queue | Stack |
|-------|-------|
| FIFO | LIFO |
| Insert Rear | Push Top |
| Delete Front | Pop Top |

## Applications
- CPU Scheduling
- Printer Queue
- BFS
- Task Scheduling
- Networking
