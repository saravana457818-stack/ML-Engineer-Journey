# DSA Notes -- Recursion

## What is Recursion?

Recursion is a programming technique where a function calls itself to
solve a smaller version of the same problem until it reaches a **base
case**.

### General Structure

``` python
def recursive_function():
    if base_case:
        return
    recursive_function()
```

------------------------------------------------------------------------

## Components of Recursion

### 1. Base Case

The stopping condition that prevents infinite recursion.

``` python
def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
```

### 2. Recursive Case

The part where the function calls itself with a smaller input.

``` python
count(n-1)
```

### 3. Call Stack

Every recursive call is stored in the call stack. When the base case is
reached, calls return in reverse (LIFO).

Example:

    factorial(3)
    ↓
    factorial(2)
    ↓
    factorial(1)
    ↓
    return

------------------------------------------------------------------------

# Recursive Programs

## Factorial

``` python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
```

## Fibonacci

``` python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Sum of N Numbers

``` python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)
```

## Power of a Number

``` python
def power(a,b):
    if b == 0:
        return 1
    return a * power(a,b-1)
```

------------------------------------------------------------------------

# Time Complexity

  Problem                       Complexity
  ----------------------------- ------------
  Factorial                     O(n)
  Sum of N                      O(n)
  Power                         O(n)
  Fibonacci (basic recursion)   O(2\^n)

------------------------------------------------------------------------

# Common Mistakes

-   Forgetting the base case
-   Infinite recursion
-   Recursive call doesn't move toward the base case
-   Stack overflow due to deep recursion

------------------------------------------------------------------------

# LeetCode Practice

1.  Climbing Stairs (#70)
2.  Binary Search (#704) -- Revision

------------------------------------------------------------------------

# Interview Questions

1.  What is recursion?
2.  What is a base case?
3.  What is a recursive case?
4.  Explain the call stack.
5.  Advantages and disadvantages of recursion.
6.  Difference between recursion and iteration.

------------------------------------------------------------------------

# Quick Revision

-   **Recursion:** Function calls itself.
-   **Base Case:** Stops recursion.
-   **Recursive Case:** Continues recursion.
-   **Call Stack:** Stores active recursive calls.
-   Always move toward the base case.
