# DSA Notes - Binary Search & Stack

# Binary Search

## What is Binary Search?
Binary Search is a searching algorithm that works only on **sorted arrays/lists**.
Instead of checking every element, it repeatedly divides the search space into half.

Time Complexity: **O(log n)**
Space Complexity:
- Iterative: O(1)
- Recursive: O(log n)

---

## Preconditions
- Data must be sorted.
- Random access structure (like Python list).

---

## Algorithm
1. Set `start = 0`
2. Set `end = len(arr) - 1`
3. Find middle:
```python
mid = (start + end) // 2
```
4. If `arr[mid] == target`, return index.
5. If target is greater, search right half.
6. Else search left half.
7. Repeat until found or `start > end`.

---

## Common Mistake

❌ Wrong:
```python
mid = start + end / 2
```

✅ Correct:
```python
mid = (start + end) // 2
```

---

## Iterative Binary Search

```python
while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
```

---

## Binary Search Applications
- Search in sorted arrays
- Lower Bound / Upper Bound
- Finding first or last occurrence
- Searching answer space

---

# Stack

## What is a Stack?

A Stack follows the **LIFO (Last In, First Out)** principle.

Example:
```
Top
30
20
10
```

---

## Operations

### Push
Adds an element.

```python
stack.append(10)
```

Time: O(1)

---

### Pop
Removes the top element.

```python
stack.pop()
```

Time: O(1)

---

### Peek / Top

```python
stack[-1]
```

Time: O(1)

---

### isEmpty

```python
len(stack) == 0
```

---

## Stack using Python List

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
print(stack[-1])
```

---

## Applications of Stack

- Undo / Redo
- Browser Back button
- Function Call Stack
- Parentheses Matching
- Expression Evaluation
- DFS (Depth First Search)

---

# Binary Search vs Linear Search

| Feature | Linear Search | Binary Search |
|---------|---------------|---------------|
| Works on | Any array | Sorted array |
| Time | O(n) | O(log n) |
| Faster | No | Yes |

---

# Quick Revision

## Binary Search
- Sorted array required
- Divide into halves
- Time: O(log n)

## Stack
- LIFO
- Push
- Pop
- Peek
- Time for push/pop: O(1)

---

# Interview Questions

1. Why must Binary Search use a sorted array?
2. Difference between Linear Search and Binary Search?
3. What is LIFO?
4. Difference between Stack and Queue?
5. Real-life applications of Stack?
6. Why is Binary Search O(log n)?
