# Exercise 2.1: Lists and List Comprehension

random_numbers = [44, -9321, -+12, -0.2, --9, 3, 4, +-5, 3029, 231, ---3]

positive_numbers = [number for number in random_numbers if number >= 0]

for number in positive_numbers:
    print(number)
