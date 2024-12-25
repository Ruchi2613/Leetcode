# # * works with iterables (like lists, tuples) to unpack or pack positional arguments.
# # ** works with dictionaries to unpack or pack keyword arguments.
#
#
# 1. Dict :
my_dict = {"b": 2, "c": 3}
new_entry = {"a": 1}
c_entry = {"z":24}

my_dict = {**new_entry, **c_entry,**my_dict}

print(my_dict)

# 2.
my_dict = {"b": 2, "c": 3}
a = {"a": 1, **my_dict}

print(a)

3.
'''
Python | Check order of character in string using OrderedDict( )
Given an input string and a pattern, check if characters in the input string 
follows the same order as determined by characters present in the pattern. 
Assume there won’t be any duplicate characters in the pattern. Examples:
Input: 
string = "engineers rock"
pattern = "er";
Output: true
Explanation: 
All 'e' in the input string are before all 'r'.

Input: 
string = "engineers rock"
pattern = "gsr";
Output: false
Explanation:
There are one 'r' before 's' in the input string.
'''


def check_order(string, pattern):
    i, j = 0, 0
    for char in string:
        if char == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
        i += 1

    return False


string = 'engineers rock'
pattern = 'gsr'
print(check_order(string, pattern))


# 4.Dictionary and counter in Python to find winner of election

votes =['john','johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john']

dict = {}

for i in range(len(votes)):
    if votes[i] in dict:
        dict[votes[i]] +=1
    else:
        dict[votes[i]] = 1

max = float('-inf')
key_max = ''
for k,v in dict.items():
    if v > max:
        max = v
        key_max = k
    elif v == max and k < key_max:
        key_max = k
print("Winner:", key_max)


#5. Python – Append Dictionary Keys and Values ( In order ) in dictionary
'''
Given a dictionary, perform append of keys followed by values in list.

Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3} 
Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3] 
Explanation : All the keys before all the values in list. 

Input : test_dict = {“Gfg” : 1, “Best” : 3} 
Output : [‘Gfg’, ‘Best’, 1, 3] 
Explanation : All the keys before all the values in list.
'''

test_dict = {'Gfg' : 1,
             'is' : 2,
             'Best': 3}
list_key = list(test_dict.keys())
list_val = list(test_dict.values())

listt = list_key + list_val
print(listt)


#6. Sort Python Dictionary by Key or Value – Python

d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

sorted_keys = sorted(d.keys())

sorted_dict = {}
for key in sorted_keys:
    sorted_dict[key] = d[key]

print(sorted_dict)


#7.Python – Sort Dictionary key and values List
test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}

d = {}

for x in sorted(test_dict):
    d[x] = sorted(test_dict[x])

print(d)



#8.Print anagrams together in Python using List and Dictionary

def allAnagram(input):

    dict = {}

    for strVal in input:

        key = ''.join(sorted(strVal))

        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)


    output = ""
    for key, value in dict.items():
        output = output + ' '.join(value) + ' '

    return output

print(allAnagram(input=['cat', 'dog', 'tac', 'god', 'act']))

#9.Python Counter to find the size of largest subset of anagram words


def allAnagram_len(input):

    dict = {}

    for strVal in input:

        key = ''.join(sorted(strVal))

        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key]=[strVal]


    # print(dict)

    max_size = 0
    for key, val in dict.items():
        max_size = max(len(val), max_size)

    return max_size
print(allAnagram_len(input=['cat', 'dog', 'tac', 'god', 'act']))



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

# 1.

from operator import itemgetter

people = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19}
]

# Sort by "age" and then by "name"
sorted_people = sorted(people, key=itemgetter("age", "name"))
print(sorted_people) #[{'name': 'Nikhil', 'age': 19}, {'name': 'Manjeet', 'age': 20}, {'name': 'Nandini', 'age': 20}]

#2.
from operator import itemgetter

data = [(1, "b", 3), (2, "a", 2), (3, "c", 1)]

# Sort by the second element (index 1)
sorted_data = sorted(data, key=itemgetter(1))
print(sorted_data) #[(2, 'a', 2), (1, 'b', 3), (3, 'c', 1)]


'''Lambda:'''

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







