# class AskMovieName: # Note: Made the class name PascalCase to follow Python conventions.
#
#     def __init__(self):
#         self.movie_name = []
#
#     def insert_movie_name(self):
#
#         while len(self.movie_name) < 3:
#             get_movie_name = str(input("Enter 3 movie name:"))
#
#             if get_movie_name in self.movie_name:
#                 print("You've already entered this movie. Please enter a different movie.")
#                 continue
#
#             self.movie_name.append(get_movie_name)
#
#             if len(self.movie_name) ==1:
#                 print(f"please enter 2 other movie name but not same movie name as,{get_movie_name}")
#             elif len(self.movie_name) == 2:
#                 print(f"please enter 1 other movie name but not same movie name as,{self.movie_name[0:2]}")
#             else:
#                 print("Please enter 3 movies name")
#
#         return f"Thank you! here are your 3 movie names:{self.movie_name}"
# cl = AskMovieName()
# print(cl.insert_movie_name())
#
#
#
# '''Optimized'''
#
#
# class AskMovieName: # Note: Made the class name PascalCase to follow Python conventions.
#
#     def __init__(self):
#         self.movie_names = []
#
#     def insert_movie_name(self):
#
#         while len(self.movie_names) < 3:
#             remaining_movie_name = 3 - len(self.movie_names)
#             get_movie_name = str(input(f"Enter {remaining_movie_name} movie name:"))
#
#             if get_movie_name in self.movie_names:
#                 print("You've already entered this movie. Please enter a different movie.")
#                 continue
#
#             self.movie_names.append(get_movie_name)
#
#
#             if remaining_movie_name > 0:
#                     print(f"Please enter {abs(len(self.movie_names)-3)} more movie name(s).")
#
#         return f"Thank you! here are your 3 movie names:{self.movie_names}"
# cl = AskMovieName()
# print(cl.insert_movie_name())
#


'''DICTIONARY'''


# marks = {}
#
# x = int(input("Enter the marks:"))
# marks.update({"maths":x})
#
# x = int(input("Enter the marks:"))
# marks.update({"Phy":x})
#
# x = int(input("Enter the marks:"))
# marks.update({"chem":x})
#
#
# print(marks)

# li = []
#
# i = 1
# while i <= 10:
#     li.append(i*i)
#     i+=1
# print(li)

# nums = (1,2,3,4,5,690,45,67,36,78,90,36)
#
# target = 36
# i = 0
# while i < len(nums):
#     if nums[i]== target:
#         print("found at index:", i)
#     else:
#         print("finding...")
#     i+=1

'''TUPLE'''

nums = (1, 2, 3, 4, 5, 690, 45, 67, 36, 78, 90, 36)
idx = 0
target = 36

for el in nums:
    if el == target:
        print("number found at idx:",idx)
    idx+=1

'''Normal loop'''
sequence = range(5)

for i in sequence:
    print(i)

eequence = range(2,10)

for i in eequence:
    print(i)


'''While loop'''

sum = 0
i = 0

while i<=5:
    sum+=i
    i+=1
print("sum:", sum)








