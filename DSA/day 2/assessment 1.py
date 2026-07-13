class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item. Raise an error if empty."""
        if self.is_empty():
            return "Stack Underflow: The stack is empty!"
        
        removed_item = self.stack.pop()
        return f"Popped: {removed_item}"

    def peek(self):
        """Look at the top item without removing it."""
        if self.is_empty():
            return "Stack is empty!"
        return f"Top element: {self.stack[-1]}"

    def size(self):
        """Return the current size of the stack."""
        return len(self.stack)

    def display(self):
        """Print the current state of the stack."""
        print("Current Stack (Top -> Bottom):", self.stack[::-1])


# --- Driver Code to Test the Stack ---
if __name__ == "__main__":
    my_stack = Stack()

    # 1. Check if empty
    print(f"Is stack empty? {my_stack.is_empty()}") 

    # 2. Push elements
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    
    my_stack.display() # Should show [30, 20, 10]

    # 3. Peek at the top element
    print(my_stack.peek()) 

    # 4. Pop elements
    print(my_stack.pop()) # Removes 30
    print(my_stack.pop()) # Removes 20

    my_stack.display() # Should show [10]
    
    # 5. Check size
    print(f"Stack size: {my_stack.size()}")