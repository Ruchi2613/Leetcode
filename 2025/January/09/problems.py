#1. Longest sub-array having sum k

def lenOfLongSubarr(arr, k):
    res = float('-inf')
    for i in range(len(arr)):
        total_sum = 0
        for j in range(i,len(arr)):
            total_sum += arr[j]
            if total_sum == k:
                res = max(res,j-i+1)
            elif total_sum > k:
                break
    return res

print(lenOfLongSubarr(arr=[10, 5, 2, 7, 1, 9],k = 15))


#2.

def lenOfLongSubarr(arr, k):
    start = 0
    total_sum = 0
    res = 0

    end = 0
    while end < len(arr):
        total_sum += arr[end]

        while total_sum > k and start <= end:
            total_sum -= arr[start]
            start += 1

        if total_sum == k:
            res = max(res, end - start + 1)

        end += 1

    return res

print(lenOfLongSubarr(arr=[10, 5, 2, 7, 1, 9], k=15))


'''2.Longest Substring With K Unique Characters'''

def longestKSubstr(strr, k):

    i , j = 0,0
    res = 0
    d = {}

    while j < len(strr):

        if strr[j] not in d:
            d[strr[j]] = 1
        else:
            d[strr[j]] +=1

        while len(d) > k:
            d[strr[i]]-=1
            if d[strr[i]] == 0:
                del d[strr[i]]
            i += 1

        if len(d) == k:
            res = max(res,j-i+1)

        j += 1

    return res

print(longestKSubstr(strr= 'aabacbebebe',k = 3))


'''3.Longest Substring With Without Repeating Characters'''

def longestUniqueSubstr(strr):

    i , j = 0,0
    d = {}
    res = 0

    while j < len(strr):

        if strr[j] not in d:
            d[strr[j]] = 1

        else:
            res = max(res, len(d.keys()))
            while strr[j] in d:
                del d[strr[i]]
                i += 1
            d[strr[j]] = 1

        j+=1

    return res


print(longestUniqueSubstr(strr='geeksforgeeks'))



