# Using a comprehension to generate a list of square numbers
squares = [x**2 for x in range(1, 11)]
print(squares)

# Using a comprehension to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]
print(upper_names)

name_letters = [name for name in 'python']
print(name_letters)
