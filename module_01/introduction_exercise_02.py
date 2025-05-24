# Exercise 1.2: Control Flow - If-Else Statements
user_input: str = input('Enter a number: ')

number = int(user_input)

if number & 1:
    print('Even')
else:
    print('Odd')
