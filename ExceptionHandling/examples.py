def factorial(n):
    # n! cam also be defined as n * (n-1)
    """calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    print(factorial(20))
except (RecursionError, ZeroDivisionError):
    print("This program cannot calculate factorials that large")

print("Program terminating")