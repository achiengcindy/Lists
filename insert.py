# use the languages list we defined in the above example.
# This time insert 'c' at the first index

# define a list
languages = ['java', 'python', 'perl', 'ruby', 'c#']

# insert c in the first position
languages.insert(0, 'c')
print(languages)  # ['c', 'java', 'python', 'perl', 'ruby', 'c#']

# insert kotlin in the third position
languages.insert(2, 'Kotlin')
print(languages)  # ['c', 'java', 'python', 'perl', 'ruby', 'c#']
