# Exercise 2.4: Error Handling - Dividing Numbers

def divide_numbers(a, b) -> None:
    try:
        num1 = float(a.strip())
        num2 = float(b.strip())
        result = num1 / num2
        print(f'Result: {num1} / {num2} = {result}')
    except ValueError as err:
        print(f'Error: {str(err)}. Please enter valid numeric values.')
    except ZeroDivisionError as err:
        print(f'Error: {str(err)}. Please enter a number >= 0.')

if __name__ == '__main__':
    n1 = input('Enter 1st number: ')
    n2 = input('Enter 2nd number: ')
    divide_numbers(n1, n2)
