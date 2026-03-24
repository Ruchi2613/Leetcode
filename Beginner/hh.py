
# 1.
# def print_pattern(n):
#    for i in range(1, n + 1):
#        for j in range(1, i + 1):
#            print(j, end=" ")
#        print()
# print_pattern(n=4)

#2.
# def print_pattern(n):
#    for i in range(n, 0,-1):
#        for j in range(1, i + 1):
#            print('*', end=" ")
#        print()
# print_pattern(n=4)

# 3.B shaped

# def print_b_pattern(n):
#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print('*', end=" ")
#         print()
#
#     for i in range(2, n + 1):
#         for j in range(1, i + 1):
#             print('*', end=" ")
#         print()
#
# print_b_pattern(n=4)

#4.

# def print_up_pattern(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ", end="")
#         for j in range(2 * (n - i) - 1):
#             print("*", end="")
#         print()
#
# print_up_pattern(n = 4)

# def print_up_pattern(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ", end="")
#         for j in range(2 * (n - i) - 1):
#             print("*", end="")
#         print()
#
# print_up_pattern(n = 4)


# def rev_star(n:int):
#
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print(" ",end='')
#         for j in range(i):
#             print('*',end="")
#         print()
#
# print(rev_star(n = 6))



# def count_digit(n):
#     if n == 0:
#         return 1
#
#     count = 0
#     while n != 0:
#         n = n // 10
#         count += 1
#
#     return count
#
# print(count_digit(n= 1234))

# def palindrome_check(arr):
#
#     if arr == arr[::-1]:
#         return f"{arr} is Palindrome"
#     else:
#         return f"{arr} is not Palindrome"
#
# print(palindrome_check(arr=[1,2,3]))


# def mean_median(arr):
#     arr.sort()
#     mean = 0
#     median = 0
#     len_n = len(arr)
#
#
#     for i in range(len(arr)):
#         mean += arr[i]
#
#     if len_n % 2 == 0:
#         num1 = (len(arr)//2)-1
#         num2 = len(arr)//2
#         median = (arr[num1]+arr[num2])/2
#     else:
#         median = arr[len(arr) // 2]
#
#     return f"The mean value of the array is {mean/len(arr)} and the median value is {median}"
#
#
# print(mean_median(arr=[1, 3, 4, 2, 6, 5, 8, 7]))
#
#
# def sum_of_palindrome(n:int):
#
#     digit_sum = 0
#     while n > 0:
#         digit_sum += n % 10
#         n //= 10
#
#     # Step 2: Check if the sum is a palindrome
#     digit_sum_str = str(digit_sum)
#     print(digit_sum_str)
#     if digit_sum_str == digit_sum_str[::-1]:
#         return "Yes"
#     else:
#         return "No"
# print(sum_of_palindrome(n = 51241))
#
# import argparse
# import os
# import json
#
# # File to store tasks
# TASK_FILE = "tasks.json"
#
# # Load tasks from file
# if os.path.exists(TASK_FILE):
#     with open(TASK_FILE, "r") as f:
#         tasks = json.load(f)
# else:
#     tasks = []
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Task Manager CLI')
#
#     parser.add_argument('task', nargs='?', help="Specify the task")  # 'task' is optional for list operation
#     parser.add_argument('operation', help="Operation to perform: add, remove, list")
#
#     args = parser.parse_args()
#
#     if args.operation == "add":
#         if args.task and args.task not in tasks:
#             tasks.append(args.task)
#             print(f"Task '{args.task}' has been added!")
#         else:
#             print("Error: Task description is required for 'add' operation or task already exists.")
#
#     elif args.operation == "remove":
#         if args.task in tasks:
#             tasks.remove(args.task)
#             print(f"Task '{args.task}' has been removed!")
#         else:
#             print(f"Error: Task '{args.task}' not found in the list.")
#
#     elif args.operation == "list":
#         if tasks:
#             print("Here are your tasks:")
#             for idx, task in enumerate(tasks, start=1):
#                 print(f"{idx}. {task}")
#         else:
#             print("No tasks available.")
#
#     else:
#         print(f"Error: Operation '{args.operation}' not recognized.")
#
#     # Save tasks to file
#     with open(TASK_FILE, "w") as f:
#         json.dump(tasks, f)
