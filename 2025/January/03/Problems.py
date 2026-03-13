'''163. Missing Ranges'''

def missing_ranges(nums,lower,upper):

    list_miss_r = []

    if len(nums) == 0:
        return list_miss_r.append([lower,upper])

    if lower < nums[0]:
        list_miss_r.append([lower,nums[0]-1])



    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] <= 1:
            continue
        else:
            list_miss_r.append([nums[i]+1,nums[i+1]-1])

    if upper > nums[len(nums)-1]:
        list_miss_r.append([nums[len(nums)-1]+1,upper])

    return list_miss_r


print(missing_ranges(nums = [0,1,3,50,75], lower = 0, upper = 99))


'''169. Majority Element'''


def majorityElement(nums):
    count_dict = {}
    # n = len(nums)
    num_num = len(nums)//2

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count > num_num:
            return num
print(majorityElement(nums = [3,2,3]))



'''349. Intersection of Two Arrays'''


def intersection(nums1, nums2):


    set_nums1 = set(nums1)
    intersection_st = set()

    for n in nums2:
        if n in set_nums1:
            intersection_st.add(n)
    return list(intersection_st)

print(intersection(nums1 = [1,2,2,1], nums2 = [2,2]))


'''485. Max Consecutive Ones'''


def findMaxConsecutiveOnes(nums):
    count = 0
    maxi = float('-inf')

    for x in nums:
        if x == 1:
            count += 1
        else:
            count = 0
        maxi = max(count, maxi)

    return maxi

print(findMaxConsecutiveOnes(nums=[1,1,0,1,1,1]))

