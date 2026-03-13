'''

### **1. Hash Function**
- A hash function takes a key (like a name) and turns it into a number (called an index).
- Example:
  If the key is `"Alice"`, the hash function gives the number `5`.

---

### **2. Hashtable**

- A hashtable is like a storage box with many slots.
- The hash function decides in which slot the data will go.
- Example:
  If the hash function says `5`, then `"Alice's data"` will be stored in slot `5`.



### **3. Dictionary**

- A dictionary is a ready-made tool that uses a hash function and hashtable inside, but you don’t need to worry about how it works.
- You just store and retrieve data using key-value pairs.
- Example in Python:
  ```python
  my_dict = {"Alice": "1234", "Bob": "5678"}
  print(my_dict["Alice"])  # Output: 1234
  ```

---

### **Simple Summary**
1. **Hash Function**: Changes a key (like `"Alice"`) into a number (like `5`).
2. **Hashtable**: Stores the data in the slot given by the hash function.
3. **Dictionary**: A tool that uses hash functions and hashtables to make storing and finding data easy for you.

'''

# 682. Baseball Game:
'''
682. Baseball Game
Easy
Topics
Companies
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
 

Constraints:

1 <= operations.length <= 1000
operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
For operation "+", there will always be at least two previous scores on the record.
For operations "C" and "D", there will always be at least one previous score on the record.
'''


# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#
#         stack = []
#
#         for op in operations:
#             if op == '+':
#                 stack.append(stack[-1] + stack[-2])
#             elif op == 'C':
#                 stack.pop()
#             elif op == 'D':
#                 stack.append(2 * stack[-1])
#             else:
#                 stack.append(int(op))
#         return sum(stack)



'''
2.
645. Set Mismatch
Easy
Topics
Companies
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

'''
def findErrorNums(nums):

    res = [0,0]
    for x in range(1,len(nums)+1):
        if x not in nums:
            res[1] = x
        elif nums.count(x)==2:
            res[0] = x
    return res
print(findErrorNums(nums= [1,2,2,4]))


def findErrorNums(nums):
    res = [0, 0]
    n = len(nums)

    for x in nums:
        if nums.count(x) == 2:
            res[0] = x
            break

    for x in range(1, n + 1):
        if x not in nums:
            res[1] = x
            break

    return res
print(findErrorNums(nums=[1, 2, 2, 4]))

'''
3.
643. Maximum Average Subarray I
Easy
Topics
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

'''

def findMaxAverage(nums,k):
    maxi = 0
    summ = 0


    for i in range(len(nums) - k + 1):
        j = i+(k-1)
        summ = sum(nums[i:j+1])
        maxi = max(summ/k,maxi)

    return maxi

print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))


# 2. solution:
def findMaxAverage(nums,k):

    avg_sum = float('-inf')
    sum_num = 0
    l = 0

    for r in range(len(nums)):

        sum_num+=nums[r]

        if r-l+1 == k:
            avg_sum = max(avg_sum,sum_num/k)
            sum_num -=nums[l]
            l+=1
    return avg_sum
print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
