# define a list
languages = ['java', 'python', 'perl', 'ruby', 'C#']
# slicing everything up to but not including index 3
first_three = languages[:3]
print(first_three)  # ['java', 'python', 'perl']

# slicing everything from index 3 to the last item
third_last = languages[3:]
print(third_last)  # ['ruby', 'c#']

# elements from beginning to end
list_all = languages[:]
print(list_all)  # ['java', 'python',''perl','ruby', 'c#']

# elements from 1st to 3rd item
languages[0:3]
print(languages[0:3])  # ['java', 'python', 'perl']

# last three elements
list_three = languages[-3:]
print(list_three)  # ['perl','ruby', 'c#']
