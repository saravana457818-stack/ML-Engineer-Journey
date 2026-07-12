

expenses = [2200, 2350, 2600, 2130, 2190]
first = expenses[1] - expenses[0]
print("the dollars spent extra in feb than jan is:", first)
second=expenses[0]+expenses[1]+expenses[2]+expenses[3]
print("the total amount spent in quater is:",second)
print("3. Did you spend exactly $2000 in any month?", 2000 in expenses)
expenses.append(1980)
print("june month expenses",expenses)
expenses[3]=expenses[3]-200
print("the new expenses is: ",expenses)