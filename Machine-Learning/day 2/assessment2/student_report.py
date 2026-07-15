import pandas as pd

try:
    df = pd.read_csv("ML/day 2/assessment2/studentdetails.csv")
except pd.errors.EmptyDataError:
    df = pd.DataFrame(columns=["Name", "Age", "Marks"])

while True:
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    df.loc[len(df)] = [name, age, marks]

    choice = input("Add another student? (yes/no): ").lower()

    if choice != "yes":
        break

df.to_csv("ML/day 2/assessment2/studentdetails.csv", index=False)

print("\nFinal Student Data:")
print(df)