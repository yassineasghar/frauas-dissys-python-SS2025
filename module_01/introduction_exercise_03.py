# Exercise 1.3: Loops - Creating a Multiplication Table
user_input: str = input('Enter a number: ')

number = int(user_input)
for i in range(1, 11):
    result = i * number
    print(f'{number} x {i} = {result}')
