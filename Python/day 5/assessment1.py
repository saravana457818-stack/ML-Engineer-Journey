class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)


name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

student1 = Student(name, age, marks)

student1.display()