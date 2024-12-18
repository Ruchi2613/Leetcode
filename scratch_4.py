# # def eraseOverlapIntervals(intervals):
# #     if not intervals:
# #         return 0
# #
# #     intervals.sort()
# #
# #     res = intervals[0][1]
# #     count = 0
# #
# #     for i in range(1, len(intervals)):
# #         if intervals[i][0] >= res:
# #             res = intervals[i][1]
# #         else:
# #             count += 1
# #             res = min(intervals[i][1], res)
# #     return count
# # print(eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
#
# #
# # def canMakeSquare(grid):
# #     for row in range(2):
# #         for col in range(2):
# #
# #             if (grid[row][col] + grid[row + 1][col] + grid[row][col + 1] + grid[row + 1][col + 1]).count('W') >= 3:
# #                 return True
# #
# #             if (grid[row][col] + grid[row + 1][col] + grid[row][col + 1] + grid[row + 1][col + 1]).count('B') >= 3:
# #                 return True
# #
# #     return False
# #
# #
# # print(canMakeSquare(grid=[["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]))
#
#
# # def similarPairs(words):
# #     char_sets = {}
# #
# #     for word in words:
# #         char_set = ''.join(sorted(set(word)))
# #         if char_set in char_sets:
# #             char_sets[char_set] += 1
# #         else:
# #             char_sets[char_set] = 1
# #
# #     print(char_sets)
# #
# #     count_pairs = 0
# #     for count in char_sets.values():
# #         if count > 1:
# #             count_pairs += (count * (count - 1)) // 2
# #     return count_pairs
# #
# # print(similarPairs(words = ["aba","aabb","abcd","bac","aabc"]))
#
# # count = 0
# # for i in range(len(words)):
# #     print(words[i])
# #     for j in range(i):
# #         print(j)
# #         if set(words[i]) == set(words[j]):
# #             print("words[i]:",words[i],"words[j]:",words[j])
# #             print("words[i]:", set(words[i]), "words[j]:", set(words[j]))
# #             count +=1
# # return count
#
#
# def multiply(num1, num2):
#
#     list1 = []
#     for x in num1:
#         x = int(x)
#         list1 += [x]
#
#     list2 = []
#     for x in num2:
#         x = int(x)
#         list2 += [x]
#
#     mul = 1
#     carry = 0
#     result = 0
#     multiplier = 1
#
#     # Perform multiplication manually
#     for a in reversed(list1):
#         inner_sum = 0
#         carry = 0
#         for b in reversed(list2):
#             inner_sum += (a * b + carry) % 10 * multiplier
#             carry = (a * b + carry) // 10
#             mul += inner_sum
#         result += mul
#         multiplier *= 10
#
#     return str(result)
#
#
# # Test cases
# print(multiply(num1 = "123", num2 = "456"))  # Output: 58

# def partitionLabels(s):
#     lastIndex = {}
#
#     for indx, chr in enumerate(s):
#         lastIndex[chr] = indx
#     # print(lastIndex)
#     res = []
#     size, end = 0, 0
#     for indx, chr in enumerate(s):
#         size += 1
#         end = max(end, lastIndex[chr])
#         # if lastIndex[chr] > end:
#         #     end = lastIndex[chr]
#         if indx == end:
#             res.append(size)
#             size = 0
#     return res
#
# print(partitionLabels(s = "ababcbacadefegdehijhklij"))
#
# def maximum69Number(num):
#         str_num = str(num)
#         for i in range(len(str_num)):
#             if str_num[i] == '6':
#                 str_num = str_num[:i] + '9' + str_num[i+1:]
#                 return int(str_num)
#         return num
# print(maximum69Number(num = 6696))

# n = [1,2,3,4]
# print(n[:3],n[2+1:])


# def luckyNumbers(matrix):
#     r = len(matrix)
#     c = len(matrix[0])
#
#     # Step 1: Find the minimum element in each row
#     min_in_rows = []
#     for i in range(r):
#         print(f"Row {i}: {matrix[i]}")
#         min_val = min(matrix[i])
#         print(f"Minimum in row {i}: {min_val}")
#         min_in_rows.append(min_val)
#
#     # Step 2: Find the maximum element in each column
#     max_in_columns = [float('-inf')] * c
#     for j in range(c):
#         # print(f"Column {j}: {[matrix[i][j] for i in range(r)]}")
#         for i in range(r):
#             if matrix[i][j] > max_in_columns[j]:
#                 max_in_columns[j] = matrix[i][j]
#         print(f"Maximum in column {j}: {max_in_columns[j]}")
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
#
#
# # Example usage:
# print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # Output: [15]
#
#
# def reorderSpaces(text):
#     space_count = text.count(' ')
#
#     words = text.split()
#
#     if len(words) > 1:
#         space_between_words = space_count // (len(words) - 1)
#         extra_spaces = space_count % (len(words) - 1)
#     else:
#         space_between_words = 0
#         extra_spaces = space_count
#
#     result = (' ' * space_between_words).join(words)
#     result = result + ' ' * extra_spaces
#
#     return result
# print(reorderSpaces(text = " practice   makes   perfect"))
#



# def rotate(nums, k):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     k %= len(nums)
#
#     for i in range(k):
#         previous = nums[-1]
#         for j in range(len(nums)):
#             nums[j], previous = previous, nums[j]
# print(rotate(nums = [1,2,3,4,5,6,7], k = 3))


# def merge_between_zeros(head):
#     result = []
#     current_sum = 0
#     in_between_zero = False
#
#     for num in head:
#         if num == 0:
#             if current_sum != 0:
#                 result.append(current_sum)
#                 current_sum = 0
#             in_between_zero = True
#         else:
#             if in_between_zero:
#                 in_between_zero = False
#             current_sum += num
#
#     if current_sum != 0:
#         result.append(current_sum)
#
#     return result
#
#
# # Example usage:
# head = [0, 1, 2, 0, 3, 3]
# output = merge_between_zeros(head)
# print(output)  # Output: [4, 11]

#
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
# print(is_prime(5))   # Output: True
# print(is_prime(10))  # Output: False

n = 4  # Number of rows

for i in range(n):
    # j controls the spaces before stars
    for j in range(i):
        print(" ", end="")
    # Print stars
    for j in range(2 * (n - i) - 1):
        print("*", end="")
    # Move to the next line after each row
    print()
