l = [1, 2, 3, 4]
print(l)

l[0] = 5
print(l)

# p = list(l)
p = l[1:]
# p = l
print(id(l))
print(id(p))
p[1] = 10
print(l)
print(p)

print(l[1:3])
print("1231243123"[1:5])

from pprint import pprint as pp
y = [list(range(x, x + 10)) for x in range(10, 50, 10)]
pp(y)

y = []
for x in range(10, 50, 10):
    temp = []
    for val in range(x, x + 10):
        temp.append(val)
    y.append(temp)

pp(y)


y = []
for x in range(0, 12, 3):
    temp = []
    for val in range(x, x + 3):
        temp.append(val)
    y.append(temp)

print("hello")
pp(y)
# print(y[1][6])
print(y)
print(y[0])
print(y[0][0])

for x in range(len(y)):
    print(y[x])
grid = y
# x -> 0, 1, 2, 3
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end="  ")
    print()

rows = len(grid)   # 4
cols = len(grid[0])    # 10
print("\n\n")
for r in range(rows):
    for c in range(cols):
        print(grid[r][c], end="  ")
    print()

print("\n\n")

# print("output:",end="\t")
# r = 0
# c = 0
# while r < len(grid):
#     while c < len(grid[r]):
#         print(grid[r][c],end="  ")
#         c +=1
#     # print(end= "\n")
#     r +=1
#     c = 0


print("output_even:",end="\n")
r = 0
c = 0
while r < len(grid):
    while c < len(grid[r]):
        if grid[r][c]%2 == 0:
            print([c,r],end=" , ")
        else:
            print(grid[r][c],end=" , ")
        c +=1
    print(end= "\n")
    r +=1
    c = 0

