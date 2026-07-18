# Day 5 – Object-Oriented Programming (OOP) Notes

## What is OOP?
Object-Oriented Programming (OOP) organizes code into objects containing data (attributes) and functions (methods).

## Class
A class is a blueprint for creating objects.

```python
class Student:
    pass
```

## Object
An object is an instance of a class.

```python
student = Student()
```

## Constructor (`__init__`)
Runs automatically when an object is created.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## self
`self` refers to the current object.

## Instance Variables
Variables unique to each object.

```python
self.name
self.roll_no
self.marks
```

## Methods
Functions inside a class.

```python
def display(self):
    print(self.name)
```

## Creating Objects
```python
student = Student('Rahul')
```

## Encapsulation
Keeping data and methods together inside one class.

Benefits:
- Cleaner code
- Better organization
- Easier maintenance
- Better security

## Practice Programs
- Student class
- BankAccount class
- Car class

## Quick Revision
| Concept | Meaning |
|---|---|
| Class | Blueprint |
| Object | Instance |
| Constructor | `__init__()` |
| self | Current object |
| Instance Variable | Object data |
| Method | Function in class |
| Encapsulation | Bundle data and methods |
