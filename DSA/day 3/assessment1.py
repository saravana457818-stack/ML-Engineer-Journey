stack = []
top = -1

def push(value):
    global top
    top += 1
    stack.append(value)
    return f"{value} pushed into the stack."

def pop():
    global top

    if top == -1:
        return "Stack Underflow"

    removed = stack.pop()
    top -= 1
    return f"{removed} popped from the stack."

def peek():
    if top == -1:
        return "Stack is empty."

    return f"Top element is {stack[top]}."



# Menu Driven Program
while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        print(push(value))

    elif choice == 2:
        print(pop())

    elif choice == 3:
        print(peek())

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please enter 1 to 4.")