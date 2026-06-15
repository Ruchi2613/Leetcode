from collections import Counter


a = 'aaadedccgggglkbb'

d = Counter(a) # {'g': 4, 'a': 3, 'd': 2, 'c': 2, 'e': 1, 'l': 1, 'k': 1, 'b': 2}

print(d)

result = sorted(d.items()) # is this automatically sorted by key? Yes, it is sorted by key in ascending order. [('a', 3), ('b', 2), ('c', 2), ('d', 2), ('e', 1), ('g', 4), ('k', 1), ('l', 1)]

print(result) # [('a', 3), ('b', 2), ('c', 2), ('d', 2), ('e', 1), ('g', 4), ('k', 1), ('l', 1)]


l = sorted(result, key = lambda x: (x[1],x[0]))
print(l) # [('e', 1), ('k', 1), ('l', 1), ('b', 2), ('c', 2), ('d', 2), ('a', 3), ('g', 4)]

l = sorted(result, key = lambda x: (-x[1],x[0]))
print(l) # [('g', 4), ('a', 3), ('b', 2), ('c', 2), ('d', 2), ('e', 1), ('k', 1), ('l', 1)]



# Lambda with easy:




b = 'aaaddccggggl'

d = Counter(b)
res1 = sorted(d.items())
print("Sort by key:",res1) # [('a', 3), ('c', 2), ('d', 2), ('g', 4), ('l', 1)]

res2 = sorted(d.items(), key = lambda x : (x[1],x[0])) 
print("Sort by freq:",res2) # [('l', 1), ('c', 2), ('d', 2), ('a', 3), ('g', 4)]

res3 = sorted(d.items(), key = lambda x : (x[1],x[0]),reverse=True)
print("Sort by freq desc but in reverse order and if same freq by key:",res3) # [('g', 4), ('a', 3), ('c', 2), ('d', 2), ('l', 1)]

res4 = sorted(d.items(), key = lambda x : (-x[1],-ord(x[0])))
print("Sort by freq desc and if same freq by key in reverse order:",res4) # [('g', 4), ('a', 3), ('d', 2), ('c', 2), ('l', 1)]
