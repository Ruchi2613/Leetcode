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

""" Handling missing keys in Python dictionaries"""

ele = {'a': 5, 'c': 8, 'e': 2}
if "q" in ele:
    print(ele["d"])
else:
    print("Key not found")



# 2.K’th Non-repeating Character in Python using List Comprehension and OrderedDict

def str_let(strr,k):

    d = {}

    for x in strr:
        if x not in d:
            d[x] = 1
        else:
            d[x]+=1
    print(d)

    res = []
    for key,val in d.items():
        if val == 1:
            res.append(key)

    print(res)
    for i in range(len(res)):
        if k <= len(res):
            return res[k-1]
        else:
            return "Less than k non-repeatin characters in input."

print(str_let(strr='geeksforgeeks', k = 3))


# 3. Python | Remove all duplicates words from a given sentence

def remov_duplicates(input):
    words = input.split()
    sett = set()
    result = []

    for word in words:
        if word not in sett:
            sett.add(word)
            result.append(word)

    return ' '.join(result)

print(remov_duplicates(input= 'Geeks for Geeks'))



#4.Python Dictionary to find mirror characters in a string


def mirror_characters(N, s):
    mirror_dict = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
        'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
        'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
        'y': 'b', 'z': 'a'
    }

    result = list(s)

    for i in range(N - 1, len(s)):
        if 'a' <= result[i] <= 'z':
            result[i] = mirror_dict[result[i]]

    return ''.join(result)


print(mirror_characters(3, 'paradox'))  # Output: paizwlc


#5.Python | Convert a list of Tuples into Dictionary

def convert_tup_dict(input):

    d = dict()
    for stu, marks in input:
        # d.setdefault(stu,[marks])
        d.setdefault(stu, marks)
    return d
print(convert_tup_dict(input= [("Nakul", 93), ("Shivansh", 45), ("Samved", 65),
          ("Yash", 88), ("Vidit", 70), ("Pradeep", 52)]))


# 6.
from collections import Counter

def makeString(str1, str2):

    dict1 = Counter(str1)
    dict2 = Counter(str2)


    result = dict1 & dict2
    return result == dict1
print(makeString(str1='ABHISHEKsinGH',str2='gfhfBHkooIHnfndSHEKsiAnG'))

# 7.Python dictionary, set and counter to check if frequencies can become same


def can_make_frequencies_same(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    print(freq)

    freq_values = list(freq.values())
    freq_set = set(freq_values)

    if len(freq_set) == 1:
        return "Yes"

    if len(freq_set) > 2:
        return "No"

    min_freq, max_freq = min(freq_set), max(freq_set)

    if freq_values.count(min_freq) == 1 and min_freq == 1:
        return "Yes"

    if max_freq - min_freq == 1 and freq_values.count(max_freq) == 1:
        return "Yes"

    return "No"



# print(can_make_frequencies_same("xyyz"))
# print(can_make_frequencies_same("xyyzz"))
print(can_make_frequencies_same("xxxxyyzz"))


# 1.Possible Words using given characters in Python
def charCount(input,charSet):
    res = []
    for x in input:
        is_valid = True
        for y in x:
            if y not in charSet:
                is_valid = False
                break
        if is_valid:
            res.append(x)
    return ' '.join(res)



print(charCount(input = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run'],
    charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']))


#2.Python – Keys associated with Values in Dictionary


def reverse_dict(test_dict):
    res = {}

    for key,value in test_dict.items():
        for val in value:
            if val not in res:
                res[val] = [key]
            else:
                res[val].append(key)
    return res


print(reverse_dict(test_dict={'abc': [10, 30], 'bcd': [30, 40, 10]}))





