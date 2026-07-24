def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

num = int(input("Enter a number: "))
print(sum_n(num))