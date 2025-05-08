# # d = {'a':3,'b':4,'c':5}
# #
# # res = d['a']
# #
# # for k,v in d.items():
# #     if res != d[k]:
# #         print("False")
# # print("True")
#
#
# class HelloRuchi:
#     def xyz(self):
#         return "hello World"
#
#
# cl = HelloRuchi()
# print(cl.xyz())
#
#
# # list1 = [1,2,5]
# # list2 = [2,4,6,7]
# # i , j = 0,0
# # res = []
# # while i < len(list1) or j < len(list2):
# #
# #         if list1[i] < list2[j]:
# #             res.append(list1[i])
# #             i+=1
# #         else:
# #             res.append(list2[j])
# #             j+=1
# #
# # # if j<len(list2):
# # #     res.extend(list2[j:])
# # #
# # # if i<len(list1):
# # #     res.extend(list1[i:])
# #
# # print(res)
# #
# #
# #         # if i == 0:
# #         #     print("hello")
# class Students:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         return f"student {self.name} got avg_score is {sum // len(self.marks)}"
#
#
# cl = Students("Ruchi", [98, 99, 97, 91])
# print(cl.get_avg())
#
#
# class Account:
#
#     def __init__(self, acc_no):
#         self.balance = 0
#         self.acc_no = acc_no
#
#     def debit(self, amount):
#         self.balance = self.balance - amount
#         return f"amount debited: {self.balance}"
#
#     def credit(self, amount):
#         self.balance = self.balance + amount
#         return f"amount credited: {self.balance}"
#
#     def print_bal(self):
#         return f"final balance:{self.balance}"
#
#
# obj = Account(1996)
# print(obj.debit(20))
# print(obj.credit(2000))
# print(obj.print_bal())
#
# # obj1 = Account(1996)
# # print(obj1.debit(20))
# # print(obj1.credit(2000))
# # print(obj1.print_bal())
# #
# # obj1 = Account(1000, 1996)
# # print(obj1.debit(19))
# # print(obj1.credit(2001))
# # print(obj1.print_bal())
#
#
# # private function:
#
#
# # class AccountCustomer:
# #
# #     def __init__(self,acc_n, acc_pass):
# #         self.acc_n = acc_n
# #         self.__acc_pass = acc_pass # this make private attribute
# #     def reset_pass(self):
# #         print(self.__acc_pass)
# #
# # cl = AccountCustomer("12345","123")
# # print(cl.acc_n)
# # # print(cl.__acc_pass) # this will not show the password becuase it is outside the class scope. if you want to then you will have to make one function inside the class scope
# # cl.reset_pass()
#
#
# class Calculator:
#
#     def __init__(self):
#         self.num1 = 0
#
#     def cal_num(self,num2,operator):
#
#         if operator == '+':
#             self.num1 = self.num1 + num2
#             # return self.num1
#         elif operator == '-':
#             self.num1 = self.num1 - num2
#             # return self.num1
#         elif operator == '*':
#             self.num1 = self.num1 * num2
#             # return self.num1
#         elif operator == '/':
#             if num2== 0:
#                 return "Choose more than 0 digit"
#             self.num1 = self.num1 / num2
#
#         return self.num1
#
# cl = Calculator()
# print(cl.cal_num(5,"+"))
# print(cl.cal_num(5,"+"))
# print(cl.cal_num(3,"/"))
# print(cl.cal_num(2,"*"))
# print(cl.cal_num(0,"/"))
# print(cl.cal_num(0,"+"))
#
#


s = 'hello, Im ruchi'
print(s.split())

n = 1
print(n//10)

s = 'abcdefgh'
print(s[::-1])

v = list('abcdefgh')
print(v[:-1])

