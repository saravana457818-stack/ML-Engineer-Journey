# Python OOP (Continued) – Complete Notes

> **Session Duration:** 1.5 Hours

## Learning Objectives

- Understand constructors (`__init__`)
- Differentiate instance variables and class variables
- Create and use instance methods
- Understand the basics of inheritance
- Override methods
- Use `super()`
- Build simple OOP-based programs

---

# 1. Constructor (`__init__`)

A **constructor** is a special method that is automatically executed whenever an object is created.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Creating an object:

```python
s1 = Student("Alice", 20)
```

### Why Use a Constructor?

Without a constructor:

```python
class Student:
    pass

s1 = Student()
s1.name = "Alice"
s1.age = 20
```

With a constructor:

```python
s1 = Student("Alice", 20)
```

- Cleaner
- Easier to maintain
- Prevents missing values

---

# 2. Instance Variables

Instance variables belong to an individual object. Each object has its own copy.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

```python
s1 = Student("Alice")
s2 = Student("Bob")
```

---

# 3. Class Variables

Class variables belong to the class and are shared by all objects.

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

---

# Instance Variable vs Class Variable

| Instance Variable | Class Variable |
|-------------------|---------------|
| Belongs to an object | Belongs to the class |
| Different for every object | Shared by all objects |
| Created using `self` | Created directly inside the class |

---

# 4. Instance Methods

Methods that work with object data.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

---

# 5. Inheritance

Inheritance allows one class to reuse another class's properties and methods.

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()
```

## Advantages

- Code reusability
- Less duplication
- Easier maintenance
- Better organization

---

# 6. Method Overriding

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
```

---

# 7. `super()`

Used to call the parent class constructor or methods.

```python
class Animal:
    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")
```

---

# Practice Programs

## Student Class

```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.marks)
```

## Employee Class

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

## Bank Account Class

```python
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
```

## Library Management Class

```python
class Library:
    def __init__(self, book):
        self.book = book

    def issue(self):
        print(self.book, "issued")

    def return_book(self):
        print(self.book, "returned")
```

---

# Challenge: Rectangle Class

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())
```

---

# Interview Questions

1. What is a constructor?
2. What is `self`?
3. What is an instance variable?
4. What is a class variable?
5. What is inheritance?
6. What is method overriding?
7. Why is `super()` used?

---

# Quick Revision

- `__init__()` → Constructor
- `self` → Current object
- Instance Variable → Unique to each object
- Class Variable → Shared among all objects
- Instance Method → Works with object data
- Inheritance → Reuse parent class features
- Method Overriding → Replace parent method
- `super()` → Access parent class functionality
