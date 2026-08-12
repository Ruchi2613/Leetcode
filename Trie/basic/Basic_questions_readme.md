# Python from Scratch — 200 Question Homework Set

**Part A:** 150 foundation questions (variables → matrices)
**Part B:** 50 time-complexity questions

**Difficulty tags:** 🟢 Easy · 🟡 Medium · 🔴 Hard

**Rules for the student**
- No AI, no Stack Overflow copy-paste. Use only the official Python docs.
- Do not use libraries (`numpy`, `itertools`, `collections`) unless a question says so.
- For every question, write the code **and** run it on at least 2 test inputs, including one edge case (empty input, single element, all-same values, negative numbers).
- If a question says "without using X", the whole point is the restriction. Respect it.

---

# PART A — FOUNDATIONS (150 questions)

## Section 1 — Variables, Types, Operators, I/O (Q1–Q12)

1. 🟢 Take a name and age as input, print `Hi <name>, next year you will be <age+1>.`
2. 🟢 Take two numbers as input and print their sum, difference, product, quotient, floor-quotient, remainder, and power.
3. 🟢 Swap two variables **without** using a third variable.
4. 🟢 Take a float input and print it rounded to exactly 2 decimal places.
5. 🟢 Print the data type of these one by one: `5`, `5.0`, `"5"`, `True`, `None`, `[5]`, `(5,)`, `{5}`, `{5:5}`.
6. 🟢 Convert `"42"` to int, `42` to string, `"3.7"` to float, and `3.7` to int. Print each result and its type. Explain in a comment why `int("3.7")` fails but `int(3.7)` does not.
7. 🟢 Take total seconds as input and print it as `H hours, M minutes, S seconds`.
8. 🟡 Take a 3-digit number and print the sum of its digits **without** converting it to a string.
9. 🟡 Predict the output first (write your guess as a comment), then run:
   `print(10 / 3, 10 // 3, 10 % 3, -10 // 3, -10 % 3)`. Explain the two negative results.
10. 🟡 Predict then run: `print(0.1 + 0.2 == 0.3)`. Explain the result and write a correct way to compare two floats.
11. 🟡 Explain with code the difference between `=`, `==`, and `is`. Show one case where `==` is `True` but `is` is `False`.
12. 🔴 Take a temperature in Celsius and print Fahrenheit and Kelvin, formatted to 1 decimal, using an f-string with alignment so all output columns line up.

## Section 2 — Conditionals, Boolean Logic, and `match` / "switch" (Q13–Q24)

13. 🟢 Take a number and print whether it is positive, negative, or zero.
14. 🟢 Take a number and print whether it is even or odd.
15. 🟢 Take 3 numbers and print the largest **without** using `max()`.
16. 🟢 Take a year and print whether it is a leap year. (Rule: divisible by 4, except centuries not divisible by 400.)
17. 🟢 Take a marks value (0–100) and print the grade: 90+ = A, 80–89 = B, 70–79 = C, 60–69 = D, below = F. Also handle invalid input outside 0–100.
18. 🟡 Take 3 side lengths and print whether they form a valid triangle, and if so whether it is equilateral, isosceles, or scalene.
19. 🟡 Write a simple calculator: take two numbers and an operator (`+ - * / %`), print the result. Handle division by zero.
20. 🟡 Rewrite Q19 using `match` / `case` (Python's "switch"). Include a `case _:` default branch.
21. 🟡 Use `match` / `case` to build a day-type checker: input a day name, output `"Weekend"` or `"Weekday"`. Use the `|` (or-pattern) so you don't repeat branches.
22. 🟡 Explain with code why Python has no C-style `switch`, and show the **dictionary dispatch** alternative: a dict mapping operator strings to lambda functions, used to build the same calculator as Q19.
23. 🟡 Predict then run each: `print(bool(0), bool(""), bool([]), bool({}), bool(None), bool("0"), bool([0]))`. Write a rule in your own words for what is falsy in Python.
24. 🔴 Take a password string and print which rules it fails: at least 8 characters, at least one uppercase, one lowercase, one digit, one symbol. Print **all** failures, not just the first one.

## Section 3 — `for` Loops and `range` (Q25–Q40)

25. 🟢 Print numbers 1 to 20, each on a new line.
26. 🟢 Print numbers 20 down to 1 using `range` with a negative step.
27. 🟢 Print all even numbers from 1 to 50 in two ways: (a) using `if` inside the loop, (b) using `range`'s step argument.
28. 🟢 Print the sum of numbers from 1 to N (input N).
29. 🟢 Print the multiplication table of N from 1 to 10.
30. 🟢 Print the factorial of N using a `for` loop.
31. 🟢 Explain in comments what each does, then run: `range(5)`, `range(2, 8)`, `range(2, 20, 3)`, `range(10, 0, -2)`, `range(5, 5)`, `range(5, 0)`. Print `list(...)` of each.
32. 🟡 Print the first N Fibonacci numbers using a `for` loop.
33. 🟡 Count how many digits are in a number using a loop (no `len(str(n))`).
34. 🟡 Reverse a number using a loop: `1234` → `4321`.
35. 🟡 Check if a number is prime using a `for` loop. Then improve it to only loop up to `sqrt(n)`.
36. 🟡 Print all prime numbers between 1 and 100.
37. 🟡 Use `enumerate()` to print each item of a list with its index, starting the count at 1.
38. 🟡 Use `zip()` to loop over two lists of equal length and print pairs. Then test / happens when the lists are different lengths.
39. 🟡 Write a `for` loop with an `else` clause that searches a list for a value and prints `"not found"` only if the loop never breaks. Explain when `for...else` runs.
40. mikl🔴 Print these patterns for N rows (input N):
    (a) right triangle of `*`
    (b) inverted right triangle
    (c) centered pyramid
    (d) hollow square
    (e) Pascal's triangle

## Section 4 — `while`, `while True`, `break`, `continue`, and Knowing When to Stop (Q41–Q55)

41. 🟢 Print 1 to 10 using a `while` loop.
42. 🟢 Print the sum of digits of a number using `while` and `% 10` / `// 10`.
43. 🟢 Take numbers from the user repeatedly until they enter `0`, then print the total.
44. 🟢 Reverse a number using a `while` loop.
45. 🟢 Write a countdown from N to `"Liftoff!"`.
46. 🟡 Write a `while True` loop that keeps asking for a number until the user types a valid integer, then prints it. Use `try/except` to catch bad input.
47. 🟡 Write a menu-driven program using `while True`: options 1 = add, 2 = subtract, 3 = exit. `break` only on option 3.
48. 🟡 Write a number-guessing game: the program picks a fixed secret (say 42), and loops with `while True` giving "too high" / "too low" hints, breaking on a correct guess. Count and print the number of attempts.
49. 🟡 Take a limit N and print all numbers from 1 to N, skipping multiples of 3, using `continue`.
50. 🟡 Write a `while` loop that computes the GCD of two numbers using the Euclidean algorithm.
51. 🟡 **Infinite-loop debugging.** Each snippet below runs forever. Fix each one and write in a comment *what the missing stop condition was*:
    ```python
    # (a)
    i = 0
    while i < 5:
        print(i)

    # (b)
    n = 10
    while n != 0:
        n -= 3
        print(n)

    # (c)
    x = 1
    while x > 0:
        x = x + 1

    # (d)
    while True:
        ans = "yes"
        if ans == "no":
            break
    ```
52. 🟡 Write the *same* task (sum numbers 1 to 100) three ways: `for` + `range`, `while`, and `while True` + `break`. Write 2–3 sentences on which is most readable and why.
53. 🟡 Write a `while` loop with an `else` clause. Show one run where the `else` executes and one where a `break` skips it.
54. 🔴 Write a retry loop: attempt an operation that "fails" the first 3 times (simulate with a counter), retrying up to a maximum of 5 attempts. If it never succeeds, print `"gave up"`. Your loop must have **both** a success exit and a failure exit.
55. 🔴 Collatz sequence: take N, and while N is not 1, halve it if even or do `3N+1` if odd, printing each step. Print how many steps it took. Test with N = 27.

## Section 5 — Strings (Q56–Q70)

56. 🟢 Take a string and print its length, uppercase, lowercase, and title case.
57. 🟢 Print a string reversed, in two ways: slicing and a loop.
58. 🟢 Count the vowels in a string.
59. 🟢 Take a sentence and count how many words it has.
60. 🟢 Take a string and print every second character using slicing.
61. 🟡 Check if a string is a palindrome, ignoring case and spaces.
62. 🟡 Remove all duplicate characters from a string, preserving the original order.
63. 🟡 Count the frequency of each character and print it as `char: count`.
64. 🟡 Take two strings and check if they are anagrams.
65. 🟡 Capitalize the first letter of every word **without** using `.title()` or `.capitalize()`.
66. 🟡 Take a sentence and print the longest word.
67. 🟡 Write a caesar cipher: shift every letter by K positions, wrapping Z → A. Keep non-letters unchanged.
68. 🟡 Explain string **immutability** with code: show that `s[0] = "X"` fails, and show the correct way to produce a modified copy.
69. 🔴 Compress a string: `"aaabbc"` → `"a3b2c1"`. If the compressed version is not shorter, return the original.
70. 🔴 Given a sentence, print each word and how many times it appears, sorted by count descending then alphabetically. Ignore punctuation and case.

## Section 6 — Lists (Q71–Q90)

71. 🟢 Create a list of 5 numbers. Print the first, last, and middle elements using indexing.
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

## Section 8 — Sets (Q98–Q107)

98. 🟢 Create a set from a list with duplicates and print the result. Note what happened to the order.
99. 🟢 Demonstrate `add`, `update`, `remove`, `discard`, `pop`, `clear`. Explain the difference between `remove` and `discard` by triggering both on a missing element.
100. 🟢 Given two sets, print their union, intersection, difference, and symmetric difference — using both operators (`| & - ^`) and method names.
101. 🟡 Given two lists, find the common elements, the elements unique to each, and the elements in either but not both.
102. 🟡 Check if one set is a subset / superset of another. Then check whether two sets are disjoint.
103. 🟡 Find the duplicate elements in a list using a set.
104. 🟡 Explain with code why `{}` creates a dict and not a set, and show the correct way to make an empty set.
105. 🟡 Time it yourself: build a list and a set of 100,000 numbers, then check membership (`in`) of a value that is not present. Print how long each takes. Explain the difference.
106. 🟡 Write a set comprehension that produces the set of squares of the numbers in a list.
107. 🔴 Given a list of student records `(name, subject)`, find students enrolled in **all** listed subjects, using set intersection.

## Section 9 — Dictionaries (Q108–Q125)

108. 🟢 Create a dict of 3 students and their marks. Print each key, each value, and each key-value pair using the right method.
109. 🟢 Add a new key, update an existing key, and delete a key. Print the dict after each step.
110. 🟢 Show the difference between `d["missing"]` and `d.get("missing")`. Then use `.get()` with a default value.
111. 🟢 Loop over a dict and print `key -> value` for each pair using `.items()`.
112. 🟢 Check whether a key exists in a dict. Then check whether a *value* exists.
113. 🟡 Count the frequency of each character in a string using a dict — **without** `collections.Counter`.
114. 🟡 Do the same as Q113 using `.get(key, 0)` in one line inside the loop, then again using `setdefault`.
115. 🟡 Given a dict of names → marks, print the name with the highest mark.
116. 🟡 Sort a dict by value ascending, then descending. Print the result as a list of tuples and as a new dict.
117. 🟡 Invert a dict: keys become values and values become keys. Then handle the case where two keys share a value (the inverted value should be a list).
118. 🟡 Merge two dicts. Show three ways: `.update()`, `{**a, **b}`, and `a | b`. Explain what happens on key conflicts.
119. 🟡 Write a dict comprehension that maps each number 1–10 to its cube. Then one that filters an existing dict to only entries with value > 50.
120. 🟡 Build a nested dict of students where each student has `marks` (a dict of subject → score). Print each student's average.
121. 🟡 Group a list of words into a dict keyed by first letter: `{"a": ["apple", "ant"], ...}`.
122. 🟡 Given a list of `(product, sales)` tuples with repeated products, produce a dict of total sales per product.
123. 🔴 Write a small phone book program with `while True`: add, search, delete, list all, exit. Store data in a dict.
124. 🔴 Given two dicts, print the keys only in the first, only in the second, in both, and the keys whose values differ.
125. 🔴 Explain with code why dict keys must be immutable. Show a working tuple key and a failing list key, and print the error.

## Section 10 — Matrices and 2D Lists (Q126–Q140)

126. 🟢 Create a 3×3 matrix as a nested list and print it row by row.
127. 🟢 Take matrix dimensions and elements from the user and print the matrix in a neat grid.
128. 🟢 Print the sum of all elements in a matrix.
129. 🟢 Print the sum of each row and each column separately.
130. 🟡 **The classic trap.** Predict then run:
    ```python
    m = [[0] * 3] * 3
    m[0][0] = 9
    print(m)
    ```
    Explain the output, then write the correct way to build a 3×3 zero matrix.
131. 🟡 Add two matrices of the same dimensions.
132. 🟡 Multiply two matrices. Validate that the dimensions are compatible first.
133. 🟡 Transpose a matrix using nested loops. Then do it in one line with `zip(*matrix)`.
134. 🟡 Print the sum of the primary and secondary diagonals of a square matrix.
135. 🟡 Find the largest element in a matrix and print its row and column index.
136. 🟡 Check whether a matrix is symmetric.
137. 🟡 Given a matrix, print all its border elements.
138. 🔴 Rotate a square matrix 90° clockwise **in place**.
139. 🔴 Print a matrix in spiral order.
140. 🔴 Search for a value in a matrix where each row and each column is sorted ascending — do it better than checking every cell. Explain your approach in comments.

## Section 11 — Functions and Recursion (Q141–Q147)

141. 🟢 Write a function that takes two numbers and returns their sum. Call it and print the result.
142. 🟢 Write a function with a default argument, then call it with and without that argument.
143. 🟡 Write a function using `*args` that sums any number of arguments, and one using `**kwargs` that prints every keyword pair.
144. 🟡 Demonstrate local vs global scope: show a variable being shadowed inside a function, then modified with `global`.
145. 🟡 **Mutable default argument trap.** Run this twice and explain:
    ```python
    def add_item(x, bag=[]):
        bag.append(x)
        return bag
    print(add_item(1)); print(add_item(2))
    ```
    Then write the correct version.
146. 🟡 Write recursive functions for: factorial, sum of 1 to N, Nth Fibonacci, and reversing a string.
147. 🔴 Write a recursive function to flatten an arbitrarily nested list: `[1,[2,[3,[4]]]]` → `[1,2,3,4]`.

## Section 12 — Mixed Capstone (Q148–Q150)

148. 🔴 **Student report system.** Store students in a dict of dicts. Support: add student, add subject marks, compute per-student average and grade, print a class-wide report sorted by average, and find the topper per subject. Menu-driven with `while True`.
149. 🔴 **Inventory manager.** Items stored as a dict of `name -> {"qty": int, "price": float}`. Support add, sell (reject if insufficient stock), restock, total inventory value, and a low-stock report (qty < 5). Validate all user input.
150. 🔴 **Text analyzer.** Given a paragraph, output: total characters, words, sentences; unique words (set); the 5 most frequent words (dict); the longest and shortest word; average word length; and a bar chart of the top 5 words drawn with `*` characters.

---

# PART B — TIME COMPLEXITY (50 questions)

**How to answer each question:**
1. Write the Big-O time complexity in terms of `n` (or the stated variable).
2. In one or two sentences, justify it — say what the dominant operation is and how many times it runs.
3. Where marked, also give the **space** complexity.

Assume all inputs are Python lists unless stated otherwise.

## B1 — Single Loops (Q1–Q10)

**Q1** 🟢
```python
def f(n):
    total = 0
    for i in range(n):
        total += i
    return total
```

**Q2** 🟢
```python
def f(arr):
    print(arr[0])
    print(arr[len(arr) // 2])
    print(arr[-1])
```

**Q3** 🟢
```python
def f(n):
    for i in range(0, n, 2):
        print(i)
```

**Q4** 🟢
```python
def f(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
```

**Q5** 🟢
```python
def f(n):
    for i in range(100):
        print(i * n)
```

**Q6** 🟡
```python
def f(arr):
    for x in arr:
        if x == 0:
            return True
    return False
```
Give the best case, worst case, and average case.

**Q7** 🟡
```python
def f(n):
    for i in range(n):
        for j in range(10):
            print(i, j)
```

**Q8** 🟡
```python
def f(n):
    total = 0
    for i in range(n):
        total += i
    for i in range(n):
        for j in range(n):
            total += j
    return total
```

**Q9** 🟡
```python
def f(arr):
    result = []
    for x in arr:
        result.append(x * 2)
    return result
```
Give **time and space**.

**Q10** 🟡
```python
def f(n, m):
    for i in range(n):
        print(i)
    for j in range(m):
        print(j)
```
Do not simplify `n` and `m` into one variable.

## B2 — Nested Loops (Q11–Q20)

**Q11** 🟢
```python
def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

**Q12** 🟡
```python
def f(n):
    for i in range(n):
        for j in range(i):
            print(i, j)
```

**Q13** 🟡
```python
def f(n):
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                print(i, j, k)
```

**Q14** 🟡
```python
def f(n, m):
    for i in range(n):
        for j in range(m):
            print(i, j)
```

**Q15** 🟡
```python
def f(matrix):
    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total
```
`matrix` is `n × m`. Then answer again for a square `n × n` matrix.

**Q16** 🟡
```python
def f(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                return True
    return False
```

**Q17** 🟡
```python
def f(n):
    for i in range(n):
        for j in range(100):
            for k in range(50):
                print(i, j, k)
```

**Q18** 🔴
```python
def f(arr):
    for x in arr:
        if x in arr:
            print(x)
```
`arr` is a list. Then answer again assuming `arr` is a set.

**Q19** 🔴
```python
def f(words):
    for w in words:
        for ch in w:
            print(ch)
```
`words` has `n` items with average length `k`. Do not call this `O(n²)`.

**Q20** 🔴
```python
def f(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i + j + k == n:
                    count += 1
    return count
```

## B3 — Logarithmic, `while`, and Divide-and-Conquer (Q21–Q30)

**Q21** 🟡
```python
def f(n):
    i = 1
    while i < n:
        i *= 2
        print(i)
```

**Q22** 🟡
```python
def f(n):
    while n > 1:
        n = n // 2
        print(n)
```

**Q23** 🟡
```python
def f(n):
    i = n
    while i > 0:
        i -= 1
        print(i)
```

**Q24** 🟡
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Q25** 🔴
```python
def f(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
```

**Q26** 🔴
```python
def f(n):
    i = 1
    while i < n:
        for j in range(n):
            print(i, j)
        i *= 3
```

**Q27** 🔴
```python
def f(n):
    i = 2
    while i < n:
        i = i * i
```

**Q28** 🔴
```python
def f(arr):
    arr.sort()
    for x in arr:
        print(x)
```
`arr` has `n` elements. What dominates?

**Q29** 🔴
```python
def f(arr, queries):
    arr.sort()
    for q in queries:
        binary_search(arr, q)
```
`arr` has `n` elements, `queries` has `q` elements.

**Q30** 🔴
```python
def f(n):
    count = 0
    i = n
    while i > 0:
        for j in range(i):
            count += 1
        i = i // 2
    return count
```

## B4 — Recursion (Q31–Q38)

**Q31** 🟡
```python
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
```
Give **time and space** (include the call stack).

**Q32** 🟡
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**Q33** 🟡
```python
def f(n):
    if n <= 1:
        return 1
    return f(n // 2) + 1
```

**Q34** 🔴
```python
def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 1)
```

**Q35** 🔴
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)   # merge is O(len(left) + len(right))
```
Give **time and space**.

**Q36** 🔴
```python
def f(n):
    if n <= 1:
        return 1
    return f(n // 2) + f(n // 2)
```
Compare your answer with Q34 and explain the difference.

**Q37** 🔴
```python
memo = {}
def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```
Give **time and space**, and compare with Q32.

**Q38** 🔴
```python
def subsets(arr):
    if not arr:
        return [[]]
    rest = subsets(arr[1:])
    return rest + [[arr[0]] + s for s in rest]
```

## B5 — Built-in Operations and Data Structures (Q39–Q46)

**Q39** 🟢 State the average-case time complexity of each, one line each:
`list` indexing · `list.append` · `list.insert(0, x)` · `list.pop()` · `list.pop(0)` · `x in list` · `len(list)` · `list.sort()`

**Q40** 🟢 State the average-case time complexity of each:
`dict[key]` lookup · `dict[key] = v` · `del dict[key]` · `key in dict` · looping over `dict.items()`

**Q41** 🟢 State the average-case time complexity of each:
`set.add` · `x in set` · `set.remove` · `set1 & set2` (sets of size `n` and `m`)

**Q42** 🟡
```python
def f(arr):
    result = []
    for x in arr:
        result.insert(0, x)
    return result
```

**Q43** 🟡
```python
def f(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False
```
Give **time and space**. Compare it with Q16.

**Q44** 🟡
```python
def f(s):
    result = ""
    for ch in s:
        result += ch
    return result
```
Strings are immutable in Python. Why does that matter here, and what is the fix?

**Q45** 🔴
```python
def f(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
```
Give the complexity, then rewrite it in `O(n)` and state the space cost of your rewrite.

**Q46** 🔴
```python
def f(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    return sorted(counts.items(), key=lambda kv: -kv[1])
```
`arr` has `n` items with `k` distinct values.

## B6 — Tricky Cases (Q47–Q50)

**Q47** 🔴 Python's `list.append` is described as `O(1)` **amortized**, not `O(1)` worst case. Explain what "amortized" means here, and describe the one situation where a single `append` costs `O(n)`.

**Q48** 🔴
```python
def f(n):
    arr = []
    for i in range(n):
        arr = arr + [i]
    return arr
```
This looks like Q9 but is not the same complexity. Explain why, and fix it.

**Q49** 🔴 For each pair, say which grows faster for large `n` and give a rough crossover intuition:
(a) `O(n)` vs `O(log n)`
(b) `O(n log n)` vs `O(n²)`
(c) `O(2ⁿ)` vs `O(n¹⁰⁰)`
(d) `O(n!)` vs `O(2ⁿ)`
(e) `O(1)` vs `O(log log n)`

**Q50** 🔴 Explain in your own words, with a code example for each:
(a) the difference between Big-O, Big-Ω, and Big-Θ
(b) why we drop constants and lower-order terms
(c) one algorithm whose best and worst cases differ, and one where they are identical
(d) a case where an `O(n²)` algorithm beats an `O(n log n)` one in practice

---

## Suggested Schedule (4 weeks)

| Week | Cover | Questions |
|---|---|---|
| 1 | Basics, conditionals, `for`/`range`, `while` | A: 1–55 |
| 2 | Strings, lists, tuples | A: 56–97 |
| 3 | Sets, dicts, matrices | A: 98–140 |
| 4 | Functions, capstones, complexity | A: 141–150, B: 1–50 |

**Submission format:** one `.py` file per section, questions separated by comment headers (`# ---- Q37 ----`). Complexity answers go in a single `complexity_answers.md` with the reasoning written out, not just the Big-O.
