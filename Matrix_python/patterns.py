
# pattern:

def patterns_1(n):

    for i in range(1,n+1):
        for j in range(i,n+1):
            print('*',end=" ")
        print()
patterns_1(n=5)



def pattern_2(n):
    for i in range(1,n+1):
        for j in range (1,i+1):
            print("*",end=" ")
        print()

pattern_2(n = 5)


def patterns_3(n):

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
patterns_3(n=5)


def patterns_3(n):

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
patterns_3(n=5)

def patterns_4(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            print(j,end=" ")
        print()

patterns_4(5)


def print_pattern(n):

   for i in range(1, n + 1):
       # inner loop to print space
       for j in range(1, n - i + 1):
           print(" ", end="")
       for j in range(1, i + 1):
           print(i, end=" ")
       print()
print_pattern(n=6)
def sum_of_array(arr: int):

    res = 0

    for x in arr:
        res+=x

    return res

print(sum_of_array([1, 2, 3]))


def largest_element_array(arr: int):

    res = arr[0]

    for x in range(1,len(arr)):
        if arr[x] > res:
            res = arr[x]

    return res

print(largest_element_array([20, 10, 20, 4, 100]))
def reverseArray(arr,d):
    c=(arr[d:])+(arr[:d])
    return c
print(reverseArray(arr= [1, 2, 3, 4, 5, 6, 7],d=2))


def reverseArray(arr,k):
    c=(arr[k:])+(arr[:k])
    return c
print(reverseArray(arr= [12, 10, 5, 6, 52, 36],k=2))


def arr_multiply(arr: int, n: int):
    prod = 1
    for x in arr:
        prod*=x
    return prod%n

print(arr_multiply(arr=[100, 10, 5, 25, 35, 14], n = 11))

def is_monotonic(arr):

    n = len(arr)
    if n <= 1:
        return True

    increasing = True
    decreasing = True

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

print(is_monotonic([6,5,4,4]))

arr = [1, 2, 3, 4, 5]
arr[0], arr[-1] = arr[-1], arr[0]

print(arr)

a = [10, 20, 30, 40, 50]

if 30 in a :
    print("true")
else:
    print("False")


a = [1, 2, 3, 4, 5]
res = []
for val in a:
    res.insert(0, val)
print(res)


a = [1, 2, 3, 4, 5]

rev = list(reversed(a))
print(rev)


a = [8, 3, 5, 1, 9, 12]
smallest = a[0]
for val in a:
    if val < smallest:
        smallest = val
print(smallest)

a = [10, 20, 4, 45, 99]

max1 = max2 = float('-inf')
for n in a:

    if n > max1:
        max2 = max1
        max1 = n

    elif n > max2 and n != max1:
        max2 = n

print(max2)


start, end = -4, 19

for num in range(start, end + 1):

    if num < 0:
        print(num, end=" ")

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):

    if num < 0:
        print(num, end=" ")


x = [[1, 2], [3, 4]]

y = [[4, 5], [6, 7]]

res = [[0, 0],
          [0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] - y[i][j]

print(res)

for r in res:
    print(r)


test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

res = 1

for x in range(len(test_list)):
    for y in range(len(test_list[x])):
        res*=test_list[x][y]

print(res)

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

res = []

for key, value in test_dict.items():
    res+=value # this is same as extend() function.

a = sorted(set(res))

print("The unique values list is :", a)

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

res = set()

for keyv in test_dict.values():
        for value in keyv:
            res.add(value)

print("The unique values list is :", res)


dict = {'a': 100, 'b': 200, 'c': 300}

res = []
for x in dict:
    res.append(dict[x])
summ = sum(res)

print("Sum:",summ)

dict = {'a': 100, 'b': 200, 'c': 300}

res = []
for x in dict:
    res.append(dict[x])
summ = sum(res)

print("Sum:",summ)


est_dict = {"Arushi": 22, "Anuradha": 21,
            "Mani": 21, "Haritha": 21}


new_dict = {}
for key, value in est_dict.items():
    if key != "Mani":
        new_dict[key] = value

print("The dictionary after remove is :",new_dict)

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value

print(d3)

d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d1.update(d2)
print(d1)


test_dict = {'month': [1, 2, 3],
             'name': ['Jan', 'Feb', 'March']}

x = list(test_dict.values())
a = x[0]
b = x[1]
d = dict()
for i in range(0, len(a)):
    d[a[i]] = b[i]
print("Flattened dictionary : ",d)



