# # a = [1,2,3]
# # print(a[::-1])
# # # a.reverse()
# # # print(a)

# # print(a[:])

# # ab = '123'
# # for i in range(len(ab)):
# #     print(int(ab[i]))
# # print(int(ab[::-1]))


# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(is_palindrome('123'))  # Output: False



# def abc(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(abc('123'))



# abc = 123
# abc = str(abc)
# print(abc)


a = 'abc'
a = a[::-1]
print(a)  # Output: 'cba'

a = 'abc'
print(a[::-1])  # Output: 'cba'

b = 123
b = str(b)
print(b[::-1])  # Output: '321'