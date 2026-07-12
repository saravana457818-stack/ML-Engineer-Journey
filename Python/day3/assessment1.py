string = input("Enter a string: ")

count = 0

for ch in string.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)