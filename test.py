# def armstrong(n):
#     pr = 0
#     res = 0
#     org_num = n
#     while n >=1:
#         res = n % 10
#         pr += res**3
#         n = n // 10
#     if org_num == pr:
#         return True
#     else:
#         return False
#
# print(armstrong(n=153))


# def sum_natural_num(n: int):
#     list_res = []
#     num_sum = 0
#
#     for i in range(1, n + 1):
#         num_sum = num_sum + i
#         list_res.append(num_sum)
#
#     return sum(list_res)
#
#
# print(sum_natural_num(n=5))


# def sum_natural_num(n: int):
#     list_res = []
#     num_sum = 0
#
#     for i in range(1, n + 1):
#         num_sum = num_sum + i
#         list_res.append(num_sum)
#
#     return sum(list_res)
#
#
# print(sum_natural_num(n=5))
#
#
# def sum_natural_num(n:int):
#     num_track = 1
#     sum_num = 0
#     count = 1
#     list_res = []
#
#     while count<=n:
#         sum_num+=num_track
#         list_res.append(sum_num)
#         num_track+=1
#         count+=1
#
#     return sum(list_res)
# print(sum_natural_num(n = 5))


# def even_odd(n: int):
#
#     if n%2 == 0:
#         return f"{n} is Even number"
#     else:
#         return f"{n} is Odd number"
#
# print(even_odd(n = 10))


# def swap_num(a,b):
#
#     a,b = b,a
#     return a,b
#
# print(swap_num(10,5))


# def num_sum(n):
#     pr = 0
#     res = 0
#     while n >=1:
#         res = n % 10
#         pr += res
#         n = n // 10
#     return pr
#
# print(num_sum(n=23))


# def sum_num_2d(matrix):
#     total_sum = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             total_sum = total_sum+matrix[i][j]
#     return total_sum
#
#
# print(sum_num_2d(matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]))


# def identify_vow_con(chr: str):
#
#     if chr not in ['a','e','i','o','u']:
#         return f"{chr} is consonent"
#     else:
#         return f"{chr} is vowel"
#
# print(identify_vow_con(chr = 'z'))

# def three_largest(a,b,c):
#
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(three_largest(10,20,30))


# def check_islower(c: str):
#     res = ''
#     for i in range(len(c)):
#         if c[i].islower():
#             res+=c[i].upper()
#         else:
#             res+=c[i]
#     return res
#
# print(check_islower(c='GeeksForGeeks'))


# def product_num(n):
#     res = 1
#     i = 0
#     while i < len(n):
#         res*=n[i]
#         i+=1
#     return res
#
# print(product_num(n= [1, 2, 3, 4, 5, 6]))


# def sum_even_odd(arr):
#     odd = 0
#     even = 0
#     i = 0
#     while i < len(arr):
#         if i % 2 == 0:
#             even+=arr[i]
#         else:
#             odd+=arr[i]
#         i+=1
#     return f"sum of even is {even} and odd is {odd}"
#
#
# print(sum_even_odd(arr=[1, 2, 3, 4, 5, 6]))
# def remove_spaces(str):
#     result=""
#     for char in str:
#         if char != ' ':
#             result+=char
#         else:
#             continue
#
#     return result
# print(remove_spaces(str= 'g e e k s'))


# def sum_of_palindrome(n:int):
#     res = 0
#
#     while n>0:
#         res+=n%10
#         n= n//10
#
#     digit_sum_str = str(res)
#     # print(digit_sum_str)
#     if res == digit_sum_str[::-1]:
#         return "Yes"
#     else:
#         return "No"
# print(sum_of_palindrome(n = 51241))


# def check_perfect_array(arr: int):
#
#     i = 1
#     n = len(arr)
#     while i < n and arr[i] > arr[i-1]:
#         i+=1
#
#     while i < n and arr[i] == arr[i-1]:
#         i+=1
#
#     while i < n and arr[i]< arr[i-1]:
#         i+=1
#
#     return i == n
#
# print(check_perfect_array(arr= [1, 1, 2, 2, 1]))


# def rev_vowels(st : str):
#     i = 0
#     j = len(st)-1
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     st = list(st)
#     while i<j:
#
#         if st[i] in vowels and st[j] in vowels:
#             st[i], st[j] = st[j], st[i]
#             i+=1
#             j-=1
#
#         elif st[i] in vowels and st[j] not in vowels:
#             j-=1
#         elif st[i] not in vowels and st[j] in vowels:
#             i += 1
#         else:
#             i += 1
#             j -= 1
#     return ''.join(st)
# print(rev_vowels(st = 'hello world'))


# def remove_vowels(st: str):
#     i = 0
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     st = list(st)
#     while i < len(st):
#         if st[i] not in vowels:
#             i+=1
#         else:
#             st.remove(st[i])
#             i+=1
#     return ''.join(st)
#
# print(remove_vowels(st = 'hello world'))


# def return_remainder(n1: int,n2: int):
#     return n1%n2
# print(return_remainder(10,2))


# def count_num_char(st : str):
#     res = []
#
#     for i in range(len(st)):
#         if st[i] not in res:
#             res.append(st[i])
#
#     return len(res)
#
# print(count_num_char(st='geeksforgeeks'))


# def loop_num_add(n: int):
#     res = 0
#
#     for i in range(1,n+1):
#         res = res+i
#     return res
# print(loop_num_add(n = 4))

# def find_divisor(n):
#
#     res = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             res.append(i)
#     return len(res)
# print(find_divisor(n = 24))


# def sumOfAP(a, d, n):
#     sum = 0
#     i = 0
#     while i < n:
#         sum = sum + a
#         a = a + d
#         i = i + 1
#     return sum
#
# print(sumOfAP(a= 1, d= 2, n= 4))

# def factorial(n):
#
#     res = 1
#     for i in range(2,n+1):
#         res*=i
#     return res
# print(factorial(n = 5))

# def two_point_distance(x1,y1,x2,y2):
#
#     return round(((x2-x1)**2 + (y2-y1)**2)**0.5,2)
#
# print(two_point_distance(x1 = 3, y1 = 4, x2= 4 , y2 = 3))


# def retrieve_num(st: str):
#     a = ''
#     for i in st:
#         if i.isdigit():
#             a += i
#         elif a and a[-1] != ' ':
#             a += ' '
#     return a.strip()
#
# print(retrieve_num("Hey,500 rupees and 100 h 2 j 000"))


# def retrieve_num(st: str):
#     a = ''
#     for i in st:
#         if i.isalpha():
#             a += i
#         elif a and a[-1] != ' ':
#             a += ' '
#     return a.strip()
#
# print(retrieve_num("Hey everyone, I have 500 rupees and I would spend a 100"))


# def longest_name(arr: str):
#     max_len = 0
#     listt = []
#     for i in range(len(arr)):
#         max_len = max(max_len, len(arr[i]))
#
#         while listt and len(listt[-1]) < len(arr[i]):
#             listt.pop()
#         if len(arr[i]) == max_len:
#             listt.append(arr[i])
#     return ' '.join(listt)
# print(longest_name(arr=["GeeksforGeeks", "FreeCodeCamp", "StackOverFlow", "MyCodeSchool",'xxxxxxxxxxxxxxxxxxx']))

#
# def print_floyd_triangle(n: int):
#     num = 1
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(num,end=" ")
#             num+=1
#         print()
#
#
# print_floyd_triangle(n=3)


# def cube_root(n : int):
#     return round(n**(1/3),2)
#
# print(cube_root(n = 3))

# def matrix_identical(a,b):
#     n = 4
#     for i in range(n):
#         for j in range(n):
#             if (a[i][j] != b[i][j]):
#                 return 0
#     return 1
# print(matrix_identical(a=[ [0, 1, 1, 1],
#     [2, 2, 2, 2],
#     [3, 3, 3, 3],
#     [4, 4, 4, 4]],b= [ [1, 1, 1, 1],
#     [2, 2, 2, 2],
#     [3, 3, 3, 3],
#     [4, 4, 4, 4]]))


# def automorphic_num(n: int):
#
#     res = n**2
#     res1_str = str(res)
#     n_str = str(n)
#
#     if n_str == res1_str[-len(n_str):]:
#         return True
#     else:
#         return False
#
# print(automorphic_num(n = 25))


# def automorphic_num(n: int):
#
#     res = n**2
#     res1_str = str(res)
#     # n_str = str(n)
#     match= len(str(n))
#
#     if str(n) == res1_str[-match:]:
#         return True
#     else:
#         return False
#
# print(automorphic_num(n = 25))


# def isToeplitzMatrix(mat):
#     n = len(mat)  # Number of rows
#     m = len(mat[0])  # Number of columns
#
#     # Traverse the matrix
#     for i in range(n - 1):  # Last row has no downward-right diagonal to check
#         for j in range(m - 1):  # Last column has no downward-right diagonal to check
#             if mat[i][j] != mat[i + 1][j + 1]:
#                 return False  # If a mismatch is found, it's not a Toeplitz matrix
#     return True  # If no mismatches, it's a Toeplitz matrix
#
#
# # Example usage:
# mat1 = [[6, 7, 8], [4, 6, 7], [1, 4, 6]]
# mat2 = [[6, 7, 8, 9], [4, 6, 7, 8], [1, 4, 6, 7], [0, 1, 4, 6]]
# mat3 = [[6, 3, 8], [4, 9, 7], [1, 4, 6]]
#
# print(isToeplitzMatrix(mat1))  # Output: True
# print(isToeplitzMatrix(mat2))  # Output: True
# print(isToeplitzMatrix(mat3))  # Output: False

# def getSecondLargest(arr : int):
#     largest= -1
#     sec_largest = -1
#
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             largest = arr[i]
#
#     for j in range(len(arr)):
#         if arr[j] > sec_largest and arr[j]!= largest:
#             sec_largest = arr[j]
#
#     return sec_largest
#
# print(getSecondLargest(arr=[12, 35, 1, 10, 34, 1]))
#


# def getThirdLargest(arr : int):
#     largest= -1
#     sec_largest = -1
#     third_largest = -1
#
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             largest = arr[i]
#
#     for j in range(len(arr)):
#         if arr[j] > sec_largest and arr[j]!= largest:
#             sec_largest = arr[j]
#
#     for k in range(len(arr)):
#         if arr[k]> third_largest and arr[k] != largest and arr[k]!= sec_largest:
#             third_largest = arr[k]
#
#     return third_largest

# print(getThirdLargest(arr=[12, 35, 1, 10, 34, 1]))


# def max_occuring_char(st: str):
#     d = {}
#     max = -1
#     max_char = ''
#
#
#     for i in range(len(st)):
#         if st[i] not in d:
#             d[st[i]] = 1
#         else:
#             d[st[i]]+=1
#     print(d)
#     for k,v in d.items():
#         if d[k] > max:
#             max = d[k]
#             max_char = k
#     return max_char
# print(max_occuring_char(st = 'geeksforgeeks'))

# def uncommon_char(str1,str2):
#     st1 = set()
#     st2 = set()
#
#     for ch1 in str1:
#         if ch1 not in str2:
#             st1.add(ch1)
#
#     for ch2 in str2:
#         if ch2 not in str1:
#             st2.add(ch2)
#
#     combined_list = list(st1)+list(st2)
#
#     for i in range(len(combined_list)):
#         for j in range(i+1, len(combined_list)):
#             if combined_list[i] > combined_list[j]:
#                 combined_list[i] , combined_list[j] = combined_list[j],combined_list[i]
#     return ' '.join(combined_list)
#
#
#
# print(uncommon_char("characters","alphabets"))


# def replace_0_with_5(n: int):
#         res = ''
#         n_str = str(n)
#         for i in range(len(n_str)):
#             if n_str[i] == '0':
#                 res+='5'
#             else:
#                 res+=n_str[i]
#
#         return int(res)
#
# print(replace_0_with_5(n = 102))

# def num_occuring_odd_times(arr):
#     d = {}
#
#     for num in arr:
#         if num in d:
#             d[num] += 1
#         else:
#             d[num] = 1
#     print(d)
#     for num, count in d.items():
#         if count % 2 != 0:
#             return num
#
# print(num_occuring_odd_times([1, 2, 3, 2, 3, 1, 3]))
# def num_occuring_odd_times(arr: int):
#     i = 0
#     j = len(arr) - 1
#     count = 1
#
#     while i < j:
#         if arr[i] != arr[j]:
#             j -= 1
#         elif arr[i] == arr[j]:
#             count += 1
#             j -= 1
#         if j == i:
#             if count % 2 != 0:
#                 return arr[i]
#             else:
#
#                 i += 1
#                 j = len(arr) - 1
#                 count = 1
# print(num_occuring_odd_times(arr= [1, 2, 3, 2, 3, 1, 3]))


# def earliest_repeating_chr(st:str):
#     for i in range(len(st)):
#         for j in range(i):
#             if st[i] == st[j]:
#                 return st[i]
#     return "-1"
# print(earliest_repeating_chr(st = "gekseforgeeks"))

# def earliest_repeating_chr(st: str):
#     d = {}
#
#     for i in range(len(st)):
#         if st[i] in d:
#             return st[i]
#         else:
#             d[st[i]] = i
#
#     return "-1"
#
# print(earliest_repeating_chr(st="gekseforgeeks"))


# def print_right_triangle(arr):
#     if (len(arr) < 2):
#         print("No pairs exists")
#         return
#
#
#     a = arr[0];
#     b = arr[1]
#
#
#     for i in range(0, len(arr)):
#
#         for j in range(i + 1, len(arr)):
#             if (arr[i] * arr[j] > a * b):
#                 a = arr[i];
#                 b = arr[j]
#
#
# print_right_triangle(arr=[1, 4, 3, 6, 7, 0] )


# def factorial(n):
#     fact = 1
#     res = []
#
#     for i in range(1,n):
#         fact*=i
#
#         if fact <= n:
#             res.append(str(fact))
#         else:
#             break
#     return ' '.join(res)
# print(factorial(n =100))


# def calculate_average(stream):
#     total_sum=0
#     count = 0
#
#     for x in stream:
#         count+=1
#         total_sum= total_sum+x
#         avg = total_sum/count
#         print(f"Average after {count} numbers: {avg}0")
#
# # Example usage
# stream = [10, 20, 30, 40, 50, 60]
# calculate_average(stream)


# def find_num_double(n: int):
#     for num in n:
#         if num*2 in n:
#             return num
#
# print(find_num_double(n= [2,1, 2, 3]))


# def merge_str(st1: str,st2: str):
#     i = 0
#     res = ''
#
#     while (i < len(st1)) or (i < len(st2)):
#
#         if i < len(st1):
#             res+=st1[i]
#
#         if i < len(st2):
#             res+=st2[i]
#
#         i+=1
#     return res
#
# print(merge_str(st1="geeks",st2="forgeeks"))


# def union_element(a,b):
#
#     res = []
#
#     for a_val in a:
#         if a_val not in res:
#             res.append(a_val)
#
#     for b_val in b:
#         if b_val not in res:
#             res.append(b_val)
#
#     return res
# print(union_element(a= [1,2,3,2,1],b= [3,2,2,3,3,2]))


# def intersection_with_distinct_elements(a, b):
#     result = []
#     for element in b:
#         if element in a and element not in result:
#             result.append(element)
#     return result
#
# print(intersection_with_distinct_elements(a=[1, 2, 3, 2, 1],b = [3, 2,4, 5, 6, 3]))

# def is_sorted(arr):
#     for i in range(1, len(arr)):
#         if arr[i-1] > arr[i]:
#             return "No"
#     return "Yes"
#
# print(is_sorted(arr=[20, 21, 45, 89, 89, 90]))

'''DO THIS AGAIN'''


# def fascinating(n):
#
#     res_a = n*2
#     res_b = n*3
#     final = str(n)+str(res_a)+str(res_b)
#
#     return set(final) == set('123456789')
#
# print(fascinating(n=192))


# def fascinating(n):
#
#     res_a = n*2
#     res_b = n*3
#     final = str(n)+str(res_a)+str(res_b)
#
#     for digit in '123456789':
#         if final.count(digit)!=1:
#             return False
#     return True
#
# print(fascinating(n=192))


# def square_root(n):
#
#     for x in range(1,n+1):
#         if x ** 2 == n:
#             return True
#     return False
# print(square_root(n = 4))


# def findMinDiff(arr: int, m: int):
#     arr.sort()
#     res = []
#     diff = float('inf')
#     for i in range(len(arr) - m + 1):
#         min_diff = arr[i + m - 1] - arr[i]
#         min_diff = min(min_diff, diff)
#         res.append(min_diff)
#
#     return min(res)
#
# print(findMinDiff(arr=[7, 3, 2, 4, 9, 12, 56], m=3))


# def top_5_primes():
#     primes = []
#     num = 2
#     while len(primes) < 5:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#         num += 1
#     return primes
#
# print(top_5_primes())


# def top_10_sum_primes():
#     primes = []
#     num = 2
#     while len(primes) < 10:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#         num += 1
#     return sum(primes)
#
# print(top_10_sum_primes())



# def hallow_square(n:int):
#     for i in range(1, n + 1):
#
#         if (i == 1 or i == n):
#             for j in range(1, n + 1):
#                 print("*", end="")
#
#         else:
#             for j in range(1, n + 1):
#                 if (j == 1 or j == n):
#                     print("*", end="")
#                 else:
#                     print(end=" ")
#
#         print()
# print(hallow_square(n = 5))

# 2.


