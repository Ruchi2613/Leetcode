'''1. First negative integer in every window of size k
Given an array and a positive integer k, find the first negative integer for each window(contiguous subarray) of size k. '''

def first_negative_in_window(arr, k):
    n = len(arr)
    result = []

    for i in range(n - k + 1): # I used window size. I cant use len(nums) it shows 'array index out of bound'
        for j in range(i, i + k):
            if arr[j] < 0:
                result.append(arr[j])
                break


    return result

print(first_negative_in_window(arr = [-8, 2, 3, -6, 10],k = 2))


'2. way'
def first_negative_in_window(arr, k):
    n = len(arr)
    result = []
    l = 0

    for r in range(n):
       if r-l+1 == k:
           listt = arr[l:r + 1]
           for x in listt:
                if x < 0:
                    result.append(x)
                    break
           l+=1
    return result

print(first_negative_in_window(arr = [-8, 2, 3, -6, 10],k = 2))


#2. Question:

def count_anagram(arr, pattern):
    n = len(arr)
    count = 0
    l = 0

    for r in range(n):
       if r-l+1 == len(pattern):
           listt = arr[l:r + 1]
           if sorted(listt) == sorted(pattern):
               count+= 1
           l+= 1

    return count

print(count_anagram(arr = 'forxxorfxdofr',pattern = 'for'))


'''3.'''