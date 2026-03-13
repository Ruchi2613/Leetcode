'''1. 904. Fruit Into Baskets: Medium'''

def totalFruit(fruits):
    d = {}
    res = 0
    i , j = 0,0

    while j < len(fruits):

        if fruits[j] not in d:
            d[fruits[j]] =1
        else:
            d[fruits[j]] +=1

        while len(d) > 2:
            d[fruits[i]]-=1
            if d[fruits[i]] == 0:
                del d[fruits[i]]
            i+=1

        res = max(res, sum(d.values()))

        j+=1

    return res
print(totalFruit(fruits=[1,2,3,2,2]))


'''2.724. Find Pivot Index'''

def find_pivot(nums):
    total_sum = sum(nums)
    left_sum = 0

    for ind, num in enumerate(nums):
        if left_sum == total_sum - left_sum - num:
            return ind
        left_sum += num
    return -1
print(find_pivot(nums=[1,7,3,6,5,6]))