'''71. 🟢 Create a list of 5 numbers. Print the first, last, and middle elements using indexing.
72. 🟢 Print a list forwards and backwards using slicing.
73. 🟢 Demonstrate each with output: `append`, `insert`, `extend`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, `copy`. One line of comment per method saying what it does.
74. 🟢 Find the sum, max, and min of a list **without** using `sum()`, `max()`, `min()`.
75. 🟢 Count how many even and odd numbers are in a list.
76. 🟢 Given a list, print all elements greater than a given value.
77. 🟡 Reverse a list in place **without** using `.reverse()` or slicing.
78. 🟡 Find the second-largest element in a list without sorting it.
79. 🟡 Remove duplicates from a list (a) preserving order, (b) using a set — and explain the difference in the result.
80. 🟡 Merge two sorted lists into one sorted list **without** using `sort()`.
81. 🟡 Rotate a list left by K positions.
82. 🟡 Split a list into two halves. Handle odd lengths.
83. 🟡 Write list comprehensions for: squares of 1–10; even numbers from a list; words longer than 4 letters; a flattened version of `[[1,2],[3,4],[5]]`.
84. 🟡 Write a list comprehension with an `if/else` (ternary) that turns a list of numbers into `"even"` / `"odd"` labels.
85. 🟡 Find all pairs in a list that sum to a target value.
86. 🟡 Move all zeros in a list to the end while preserving the order of the non-zero elements.
87. 🟡 **Shallow vs deep copy.** Show what happens with `b = a`, `b = a.copy()`, and `b = copy.deepcopy(a)` when `a` is a nested list. Explain each result.
88. 🔴 Implement bubble sort, selection sort, and insertion sort on a list. Print the list after every pass.
89. 🔴 Implement binary search on a sorted list, both iteratively and recursively.
90. 🔴 Given a list of numbers, find the longest run of consecutive increasing values and print that sublist.

## Section 7 — Tuples (Q91–Q97)

91. 🟢 Create a tuple, print its length, and access elements by index and by negative index.
92. 🟢 Show that a tuple is immutable: try to modify an element and print the error message you get.
93. 🟢 Unpack a tuple into separate variables. Then unpack using `*rest`.
94. 🟡 Write a function that returns multiple values, and unpack them at the call site.
95. 🟡 Convert a list to a tuple and back. Explain when you would prefer a tuple over a list.
96. 🟡 Sort a list of tuples `(name, score)` by score descending, then by name ascending. Use `sorted()` with a `key`.
97. 🔴 Show that a tuple can be a dict key but a list cannot. Then show the surprising case: a tuple containing a list is *not* hashable. Explain why.
'''


a = [1,2,3,4]
print(a.append(5)) # appends 5 to the list
print(a.remove(2)) # removes the first occurrence of 2
print(a.pop()) # removes and returns the last item
print(a.index(3)) # returns the index of the first occurrence of 3
print(a.count(4)) # counts the occurrences of 4
print(a, a.sort()) # sorts the list in place
print(a, a.reverse()) # reverses the list in place
 
b = [7,8]
print(a.extend(b)) # extends the list by appending elements from b



# 77.

def reverse_in_place(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        
        left += 1
        right -= 1
        
    return lst


# 78.
def second_largest(lst):
    
    if len(lst) < 2:
        return None

    largest = float("-inf")
    second = float("-inf")

    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            
            second = num

    if second != float("-inf"):
        return second
    else:
        return None


print(second_largest(lst=[1, 3, 4, 5, 0, 2]))