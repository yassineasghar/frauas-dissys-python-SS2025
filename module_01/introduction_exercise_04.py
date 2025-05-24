# Exercise 1.4: Functions - Fibonacci Series

def fibonacci(n: int) -> None:
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


if __name__ == '__main__':
    fibonacci(10)
