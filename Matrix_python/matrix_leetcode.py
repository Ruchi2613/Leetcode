#
# def luckyNumbers(matrix):
#     r = len(matrix)
#     c = len(matrix[0])
#
#     # Step 1: Find the minimum element in each row
#     min_in_rows = []
#     for i in range(r):
#         min_val = min(matrix[i])
#         min_in_rows.append(min_val)
#
#     # Step 2: Find the maximum element in each column
#     max_in_columns = [float('-inf')] * c
#     for j in range(c):
#         for i in range(r):
#             if matrix[i][j] > max_in_columns[j]:
#                 max_in_columns[j] = matrix[i][j]
#         # print(f"Maximum in column {j}: {max_in_columns[j]}")
#
#     # Step 3: Check for lucky numbers
#     lucky_numbers = []
#     for i in range(r):
#         for j in range(c):
#             print(f"Checking element matrix[{i}][{j}]: {matrix[i][j]}")
#             if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_columns[j]:
#                 print(f"Found lucky number: {matrix[i][j]}")
#                 lucky_numbers.append(matrix[i][j])
#
#     return lucky_numbers


# def numSpecial(mat):
#     m = len(mat)
#     n = len(mat[0])
#
#     # Calculate row sums
#     row_sums = []
#     for i in range(m):
#         row_sum = 0
#         for j in range(n):
#             row_sum += mat[i][j]
#         row_sums.append(row_sum)
#
#     # Calculate column sums
#     col_sums = []
#     for j in range(n):
#         col_sum = 0
#         for i in range(m):
#             col_sum += mat[i][j]
#         col_sums.append(col_sum)
#
#     count = 0
#
#     # Iterate through the matrix
#     for i in range(m):
#         for j in range(n):
#             if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
#                 count += 1
#
#     return count
# print(numSpecial(mat = [[1,0,0],[0,0,1],[1,0,0]]))


# def getcol(mat):
#
#     r = len(mat)
#     c = len(mat[0])
#
#     col = []
#     for x in range(c):
#         # coll = []
#         # sum_col =0
#         min = 0
#         for y in range(r):
#             # sum_col+=mat[y][x]
#             min= min(mat[y][x])
#         col.append(min)
#     print(col)
#
#
# print(getcol(mat = [[1,0,0],[0,0,1],[1,0,0]]))


# def isLongPressedName(name, typed):
#     i, j = 0, 0
#     res = []
#
#     while j < len(typed):
#
#         if i < len(name) and name[i] == typed[j]:
#             i += 1
#             j += 1
#         elif j > 0 and typed[j] == typed[j - 1]:
#             j += 1
#         else:
#             return False
#
#     return i == len(name)
# print(isLongPressedName(name = "alex", typed = "aaleexxx"))


def arrayStringsAreEqual(word1, word2) :
    string2 = ''.join(word2)
    string2_len = len(string2)
    index = 0
    for s in word1:
        for c in s:
            if index >= string2_len or c != string2[index]:
                return False
            index += 1
    return True
print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))


