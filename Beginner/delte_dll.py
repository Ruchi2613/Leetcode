# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = None
#
#
# class Solution:
#     def swapNodes(self, head: ListNode, k: int) -> ListNode:
#         # First pass: find the length of the list
#         length = 0
#         current = head
#         while current:
#             length += 1
#             current = current.next
#
#         first_k_node = head
#         for _ in range(k - 1):
#             first_k_node = first_k_node.next
#
#         second_k_node = head
#         for _ in range(length - k):
#             second_k_node = second_k_node.next
#
#         # Swap the values of the first_k_node and second_k_node
#         first_k_node.val, second_k_node.val = second_k_node.val, first_k_node.val
#
#         return head
# def max_length_between_equal_characters(s):
#     max_len = 1
#     count = 1
#
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             max_len = max(max_len, count)
#             count = 1
#
#     max_len = max(max_len, count)
#     return max_len
# print(max_length_between_equal_characters(s = "leeeeeeetttcoooooooooode"))


def k_subarray_sum(arr, k):
    subarray_sums = []

    # Initialize pointers and variables
    current_sum = 0
    left = 0

    # Traverse the array with the right pointer
    for right in range(len(arr)):
        # Add the current element to the sum
        current_sum += arr[right]

        # When the window size reaches k
        if right - left + 1 == k:
            # Append the current sum to the results list
            subarray_sums.append(current_sum)
            # Subtract the element that is sliding out of the window
            current_sum -= arr[left]
            # Move the left pointer
            left += 1

    return subarray_sums


A = [1, 1, 0, -1, -2]
A.sort()
print(A)

arr = [3, 5, 6, 2, 4, 7, 8]
k = 3
print(k_subarray_sum(arr, k))


def remove_duplicates_and_count(A):
    unique_count = 1

    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            unique_count += 1

    return unique_count


# Example usage:
print(remove_duplicates_and_count(A=[1, 2, 3, 3, 3, 4, 5, 5]))



# ans = set()
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if nums[i]+nums[j]+nums[k]==0:
#                         ans.add(tuple(sorted([nums[i],nums[j],nums[k]])))
#         return list(ans)


# def SubstringVowels( s, k):
#
#         res = []
#
#         for i in range(len(s) - k + 1):
#             count = 0
#             for j in range(i, i + k):
#                 if s[j] in ['a', 'e', 'i', 'o', 'u']:
#                     count += 1
#             res.append(count)
#         return res
# print(SubstringVowels(s= "workattech",k = 3))
#



# def cyclic_sort(arr):
#     i = 0
#     while i < len(arr):
#         correct_index = arr[i] - 1
#         if arr[i] != arr[correct_index]:
#             arr[i], arr[correct_index] = arr[correct_index], arr[i]
#         else:
#             i += 1
#     return arr
#
# array = [3, 5, 2, 1, 4]
# sorted_array = cyclic_sort(array)
# print(sorted_array)