from typing import List


def calc_sum(a,b):# function definition with parameters
    c = a+b
    return c
print(calc_sum(5,3)) # function call with arguments


def average_of_3_num(a,b,c):
    return (a+b+c)/3

print(average_of_3_num(1,1,1))



def len_of_list(nums:List[int])->int:
    count = 0
    for x in nums:
        count+=1

    return count
print(len_of_list(nums = [1,2,4,5,6,7]))


s = ['ruchi','aditya','bipin','amit']
def print_list(list_of_strings:List[str])->List[str]:
    for item in list_of_strings:
        print(item,end=" ")
print()
print(print_list(s))


'''factorial'''

def factorial(n:int)-> int:
    fact = 1
    for x in range(1,n+1):
        fact*=x
    return fact
print(factorial(n =5))


'''recursion'''
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
print(show(5))
