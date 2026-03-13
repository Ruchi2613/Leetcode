def solve(nums):
    stack = []
    curres = 0
    res = 0
    for num in nums:
        curl = 1
        while stack and stack[-1][0] >= num - curl:
            prev, l = stack.pop()
            curl = min(curl+l, num)
            curres -= (prev + prev - l + 1)*l//2
        stack.append((num, curl))
        curres += (num + num - curl + 1)*curl//2
        res = max(res, curres)
    return res

print(solve(nums=[7, 4, 5, 2, 6, 5, 12, 13, 8, 20]))
# nums = [7,4,5,2,6,5]#[7,4,5] => 3+4+5=12 is the answer
# print(solve(nums))
# nums = [7,4,5,2,6,5]
# print(solve(nums))
# print(solve([8,5,2,7,9]))