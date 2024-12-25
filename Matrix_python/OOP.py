'''itemgetter is a helper from Python's operator module that
is used to fetch specific values from objects like dictionaries, lists, or tuples.
It makes it easy to work with data when you need to sort or extract items based on certain keys or positions
'''
from operator import itemgetter

data = [(1, "b", 3), (2, "a", 2), (3, "c", 1)]

# Fetch the first and third elements from each tuple
fetch_items = itemgetter(0, 2)

# Apply to each tuple
for row in data:
    print(fetch_items(row))


# Lambda:

people = [{"name": "Nandini", "age": 20},
          {"name": "Manjeet", "age": 19}]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# ---
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)

# ---
a, b = 5,10
max_val = (lambda x,y : x if x > y else y)(a,b)
print(max_val)

# ---
a, b = 50,10
max_val = (lambda x,y : x if x > y else y)
print(max_val(a,b))
