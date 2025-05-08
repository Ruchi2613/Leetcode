'''Meta practice questions: 2025'''


# class LongestString:
#
#     def calcu_len(self,s,k):
#         s = list(s)
#         i = 0
#         count = 1
#
#         while i < len(s)-1:
#                 if s[i] == s[i+1]:
#                     count+=1
#                 else:
#                     s[i+1] = s[i]
#                     k-=1
#                     if k < 0:
#                         break
#                     count+=1
#                 i+=1
#         return count
#
# cl = LongestString()
# print(cl.calcu_len(s = 'AABABBA',k = 1))
import heapq
import sys
from operator import itemgetter
from re import split

from numpy import dtype


#
# s = 'hello, world! how are you'
# s1 = 'hello, world! how are you'
# print(len(s))
# print(s1.split(','))
# print(s1.split())
# print(list(s1))
#
#
# nums1 = [1,3,4,9,10]
# nums2 = [2,6,6,8]
# res = []
#
# i = 0
# j = 0
#
# while i < len(nums1) and j < len(nums2):
#     if nums1[i] < nums2[j]:
#         res.append(nums1[i])
#         i+=1
#     else:
#         res.append(nums2[j])
#         j+=1
#
# if i < len(nums1):
#     res.extend(nums1[i:])
# if j < len(nums2):
#     res.extend(nums2[j:])
#
# print(res)
#

#
# nums1 = [1, 3, 10, 4, 9]
# nums2 = [2, 6, 6, 8]
# res = []
#
# # Combine both arrays
# combined = nums1 + nums2
#
# # Now manually sort the combined array (no sort())
# for num in combined:
#     inserted = False
#     for i in range(len(res)):
#         if num < res[i]:
#             res.insert(i, num)
#             inserted = True
#             break
#     if not inserted:
#         res.append(num)
#
# print(res)

#meta
# str1 = "Firstly this is the first string"
# str2 = "Next is the second string"
#
# list1 = set(str1.split())
#
# list2 = set(str2.split())
# print(list1)
# print(list2)
# mismatched = []
#
# for word in list1:
#     if word not in list2:
#         mismatched.append(word)
#
# for word in list2:
#     if word not in list1:
#         mismatched.append(word)
# print(mismatched)
#
# inputDict = {"laptop": 999,
#              "smartphone": 999,
#              "smart tv": 500,
#              "smart watch": 300,
#              "smart home": 9999999}
# n: 2
#
# min_heap = []
# for x in inputDict.items():
#     key, value = x
#     heapq.heappush(min_heap, (-value, key))
#     while len(min_heap) > 2:
#         heapq.heappop(min_heap)
#
# print(min_heap[0][1])

# from collections import Counter
#
#
# def return_missing_balanced_numbers(elements):
#     frequency_map = Counter(elements)
#
#     max_frequency = max(frequency_map.values())
#
#     result = {}
#     for element, count in frequency_map.items():
#         missing_count = max_frequency - count
#         if missing_count > 0:
#             result[element] = missing_count
#
#     return result
#
# print(return_missing_balanced_numbers(elements=[1,3,4,2,1,4,1]))
#
def fill_in_the_blanks(input_lst):
    # Write your code here

    # res = []
    #
    # for i, ele in enumerate(input_lst):
    #     if i == 0 and ele == None:
    #         res.append(None)
    #     elif i > 0 and ele == None:
    #         res.append(res[i - 1])
    #     else:
    #         res.append(ele)
    #
    # return res

    res = []
    for index, value in enumerate(input_lst):
        if value is not None:
            res.append(value)
        else:
            if index > 0:
                res.append(res[index - 1])
            else:
                res.append(None)
    return res


print(fill_in_the_blanks(input_lst=[1, None, 2, 3, None, None, 5, None]))


#
# -- Find media types that contain the word 'Radio'
# WHERE media_type LIKE '%Radio%'
#
# -- Starts with 'TV'
# WHERE media_type LIKE 'TV%'
#
# -- Ends with 'Coupon'
# WHERE media_type LIKE '%Coupon'
#
# -- Contains an ampersand (multi-channel)
# WHERE media_type LIKE '%&%'
#
# -- Exclude multi-channel types
# WHERE media_type NOT LIKE '%&%'


def smallest_number_odd_digits(n):
    odd_digits = []

    while n > 0:
        digits = n % 10
        if digits % 2 != 0:
            odd_digits.append(digits)
        n = n // 10
    print(odd_digits)

    min_heap = []
    for x in odd_digits:
        heapq.heappush(min_heap, x)
    print(min_heap)

    res = []
    while min_heap:
        res.append(str(heapq.heappop(min_heap)))

    return int(''.join(res))


print(smallest_number_odd_digits(n=2359))


def unique(comments):
    values = []

    for key in comments:
        fetch_val = comments[key]
        set_val = set(fetch_val)
        values.append(set_val)
    print(values)

    d = {}

    for k in values:
        for kk in k:
            if kk in d:
                d[kk] += 1
            else:
                d[kk] = 1
    # print(d)

    max_val = -sys.maxsize
    key_ans = ''
    for k, val in d.items():
        if val > max_val:
            max_val = val
            key_ans = k
    return key_ans


print(unique(comments={"New York": ["Great service", "Nice collection", "Great service"],
                       "San Francisco": ["Nice collection", "Great service", "Helpful staff"],
                       "Chicago": ["Helpful staff", "Nice collection", "Nice collection"]}
             ))


def max_workshop(workshops):
    res = []
    for x in range(len(workshops) - 1):
        year, cl = workshops[x]["year"], workshops[x]["classes"]
        next_year, next_cl = workshops[x + 1]['year'], workshops[x + 1]['classes']
        if next_year - year == 1:
            res.append(cl + next_cl)
    print(res)

    return max(res)


print(max_workshop(workshops=[
    {"year": 2020, "classes": 10},
    {"year": 2021, "classes": 15},
    {"year": 2022, "classes": 20},
    {"year": 2023, "classes": 25},
    {"year": 2024, "classes": 30}
]))

# class LongestString:
#
#     def calcu_len(self,s,k):
#         s = list(s)
#         i = 0
#         count = 1
#
#         while i < len(s)-1:
#                 if s[i] == s[i+1]:
#                     count+=1
#                 else:
#                     s[i+1] = s[i]
#                     k-=1
#                     if k < 0:
#                         break
#                     count+=1
#                 i+=1
#         return count
#
# cl = LongestString()
# print(cl.calcu_len(s = 'AABABBA',k = 1))
import heapq
import sys
from re import split


#
# s = 'hello, world! how are you'
# s1 = 'hello, world! how are you'
# print(len(s))
# print(s1.split(','))
# print(s1.split())
# print(list(s1))
#
#
# nums1 = [1,3,4,9,10]
# nums2 = [2,6,6,8]
# res = []
#
# i = 0
# j = 0
#
# while i < len(nums1) and j < len(nums2):
#     if nums1[i] < nums2[j]:
#         res.append(nums1[i])
#         i+=1
#     else:
#         res.append(nums2[j])
#         j+=1
#
# if i < len(nums1):
#     res.extend(nums1[i:])
# if j < len(nums2):
#     res.extend(nums2[j:])
#
# print(res)
#

#
# nums1 = [1, 3, 10, 4, 9]
# nums2 = [2, 6, 6, 8]
# res = []
#
# # Combine both arrays
# combined = nums1 + nums2
#
# # Now manually sort the combined array (no sort())
# for num in combined:
#     inserted = False
#     for i in range(len(res)):
#         if num < res[i]:
#             res.insert(i, num)
#             inserted = True
#             break
#     if not inserted:
#         res.append(num)
#
# print(res)

#meta
# str1 = "Firstly this is the first string"
# str2 = "Next is the second string"
#
# list1 = set(str1.split())
#
# list2 = set(str2.split())
# print(list1)
# print(list2)
# mismatched = []
#
# for word in list1:
#     if word not in list2:
#         mismatched.append(word)
#
# for word in list2:
#     if word not in list1:
#         mismatched.append(word)
# print(mismatched)
#
# inputDict = {"laptop": 999,
#              "smartphone": 999,
#              "smart tv": 500,
#              "smart watch": 300,
#              "smart home": 9999999}
# n: 2
#
# min_heap = []
# for x in inputDict.items():
#     key, value = x
#     heapq.heappush(min_heap, (-value, key))
#     while len(min_heap) > 2:
#         heapq.heappop(min_heap)
#
# print(min_heap[0][1])

# from collections import Counter
#
#
# def return_missing_balanced_numbers(elements):
#     frequency_map = Counter(elements)
#
#     max_frequency = max(frequency_map.values())
#
#     result = {}
#     for element, count in frequency_map.items():
#         missing_count = max_frequency - count
#         if missing_count > 0:
#             result[element] = missing_count
#
#     return result
#
# print(return_missing_balanced_numbers(elements=[1,3,4,2,1,4,1]))
#
def fill_in_the_blanks(input_lst):
    # Write your code here

    # res = []
    #
    # for i, ele in enumerate(input_lst):
    #     if i == 0 and ele == None:
    #         res.append(None)
    #     elif i > 0 and ele == None:
    #         res.append(res[i - 1])
    #     else:
    #         res.append(ele)
    #
    # return res

    res = []
    for index, value in enumerate(input_lst):
        if value is not None:
            res.append(value)
        else:
            if index > 0:
                res.append(res[index - 1])
            else:
                res.append(None)
    return res


print(fill_in_the_blanks(input_lst=[1, None, 2, 3, None, None, 5, None]))


#
# -- Find media types that contain the word 'Radio'
# WHERE media_type LIKE '%Radio%'
#
# -- Starts with 'TV'
# WHERE media_type LIKE 'TV%'
#
# -- Ends with 'Coupon'
# WHERE media_type LIKE '%Coupon'
#
# -- Contains an ampersand (multi-channel)
# WHERE media_type LIKE '%&%'
#
# -- Exclude multi-channel types
# WHERE media_type NOT LIKE '%&%'


def smallest_number_odd_digits(n):
    odd_digits = []

    while n > 0:
        digits = n % 10
        if digits % 2 != 0:
            odd_digits.append(digits)
        n = n // 10
    print(odd_digits)

    min_heap = []
    for x in odd_digits:
        heapq.heappush(min_heap, x)
    print(min_heap)

    res = []
    while min_heap:
        res.append(str(heapq.heappop(min_heap)))

    return int(''.join(res))


print(smallest_number_odd_digits(n=2059))


def unique(comments):
    values = []

    # for key in comments:
    #     fetch_val = comments[key]
    #     set_val = set(fetch_val)
    #     values.append(set_val)
    # print(values)
    for key in comments.values():
        # fetch_val = comments[key]
        # set_val = set(fetch_val)
        values.extend(key)
    print(values)

    d = {}

    for k in values:
        # for kk in k:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    print(d)

    max_val = -sys.maxsize
    key_ans = ''
    for k, val in d.items():
        if val > max_val:
            max_val = val
            key_ans = k
    return key_ans


print(unique(comments=

                        {"New York": ["Great service", "Nice collection", "Great service"],
                       "San Francisco": ["Nice collection", "Great service", "Helpful staff"],
                       "Chicago": ["Helpful staff", "Nice collection", "Nice collection"]}
             ))


def max_workshop(workshops):
    res = []
    for x in range(len(workshops) - 1):
        year, cl = workshops[x]["year"], workshops[x]["classes"]
        next_year, next_cl = workshops[x + 1]['year'], workshops[x + 1]['classes']
        if next_year - year == 1:
            res.append(cl + next_cl)
    print(res)

    return max(res)


print(max_workshop(workshops=[
    {"year": 2020, "classes": 10},
    {"year": 2021, "classes": 15},
    {"year": 2022, "classes": 20},
    {"year": 2023, "classes": 25},
    {"year": 2024, "classes": 30}
]))


def maxi_book(price, budget):
    price.sort()
    left = 0
    curr_sum = 0
    max_len = 0

    for right in range(len(price)):
        curr_sum += price[right]

        while curr_sum > budget:
            curr_sum -= price[left]
            left += 1

        max_len = max(max_len, right - left + 1)
    return max_len


print(maxi_book(price=[10, 5, 2, 8, 15, 3], budget=20))


def maxi_book(price, budget):
    price.sort()
    curr_sum = 0
    count = 0

    for x in price:
        curr_sum += x

        if curr_sum <= budget:
            count += 1
        else:
            break
    return count


print(maxi_book(price=[10, 5, 2, 8, 15, 3], budget=20))


def merge_interval(sequels):
    s = sorted(sequels)

    count = 0

    for x in range(len(s) - 1):

        if s[x][1] > s[x + 1][0]:
            count += 1

    return count


print(merge_interval(sequels=[[1, 4], [2, 5], [7, 9], [3, 6], [5, 8]]
                     ))


def most_frequent_word(words_dict):
    val = []
    d = {}

    for value in words_dict.values():
        val.extend(value)
    print("hello mam:",val)

    for k in val:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    print(d)

    max_v = -sys.maxsize
    key_ans = ''
    for k, v in d.items():
        if v > max_v:
            max_v = v
            key_ans = k
    return key_ans


print(most_frequent_word(words_dict={
    "fruits": ["apple", "banana", "apple"],
    "colors": ["red", "blue", "apple"],
    "animals": ["dog", "cat", "dog"]
}))

from collections import Counter


def most_frequent_word(words_dict):
    all_words = []
    for word_list in words_dict.values():
        all_words.extend(word_list)
    print("heyy:",all_words)

    word_counts = Counter(all_words)
    print(word_counts)
    return word_counts.most_common(1)[0][0]  # [('apple', 3)]


print(most_frequent_word(words_dict={
    "fruits": ["apple", "banana", "apple"],
    "colors": ["red", "blue", "apple"],
    "animals": ["dog", "cat", "dog"]
}))


def max_num(n):
    # print('hello:',max(str(3482)))
    digit = ''
    while n > 0:
        digit += str(n % 10)  # careful str to int
        n = n // 10
    # print(digit)

    max_heap = []
    for str_n in digit:
        heapq.heappush(max_heap, int(str_n) * -1)
    print(max_heap)

    final_res = []
    while max_heap:
        final_res.append(str(heapq.heappop(max_heap) * -1))
    print(final_res)

    return int(''.join(final_res))


print(max_num(n=3482))


def consecutive_year(workshops):
    workshops.sort(key=itemgetter('year'))
    sum_num = workshops[0]['classes']
    max_num = 0


    for i in range(1,len(workshops)):
        year, cl = workshops[i]['year'], workshops[i]['classes']
        prev_yr, prev_cl = workshops[i - 1]['year'], workshops[i - 1]['classes']

        if year - prev_yr == 1 or year == prev_yr:
            sum_num += cl
        else:
            sum_num = cl
        max_num = max(max_num, sum_num)
    return max_num


print(consecutive_year(workshops=[
    {'year': 2021, 'classes': 4},
    {'year': 2019, 'classes': 3},
    {'year': 2020, 'classes': 5}

]
))

def search_element(lst, target):
    if target in lst:
        return lst.index(target)
    return 0

# Example usage
lst = [3, 5, 1, 9, 7]
target = 9
result = search_element(lst, target)
print(result)  # Output: 3 (index of the element)   