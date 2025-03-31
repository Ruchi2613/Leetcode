from typing import List


class nextGreaterElement:

    # def __init__(self):
    #     self.res = [-1] * len(nums)
    def findingelement(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:  # CHECK LOGIC
                    res[i] = nums[j]
                    break
        return f"Next Greater Element to Right: {res}"


cl = nextGreaterElement()  # dont forget ()
print(cl.findingelement(nums=[1, 3, 0, 0, 1, 2, 4]))


class nextElement:

    def findingElement(self, nums: List[int]) -> List[int]:

        '''approach:
         i starts with 4 element or last element or (n-1)
        in stack we store i+1 [] -> reverse order []

        suppose, i on 2 ele then it store i+1 i.e; 4 stack = [4]
        i on 1 ele then it store i+1 i.e; 2 stack =[4,2]

        i on 0 elem then it store i+1; 3 stack =[4,2,3]

elem -> 1  3  2  4
i ->    0  1  2  3          <- starts with n-1
        '''

        stack = []
        res = [-1] * len(nums)

        # for i in range(len(nums)-1,-1,-1):
        #
        #     if i+1 == len(nums):
        #         continue
        #     else:
        #         stack.append(nums[i + 1])
        #
        #         while stack:
        #             if stack[-1] > nums[i]:
        #                 res[i]=stack[-1]
        #                 break # dont fpregt this after append break
        #             else:
        #                 stack.pop()
        # return res

        # solution 2:

        for i in range(len(nums) - 1, -1, -1):

            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(nums[i])
        return res


'''
# Next smallest to right
nums = [6,2,5,4,5,1,6]
stack = []
res = [-1]*len(nums)
for i in range(len(nums) - 1, -1, -1):

    while stack and stack[-1] >= nums[i]:
        stack.pop()

    if stack:
        res[i] = stack[-1]

    stack.append(nums[i])
print("Next smallest to right:",res)
'''
cle = nextElement()
print(cle.findingElement(nums=[1, 3, 2, 4]))

'''Next Greater Element to Left'''


class findGreaterElementLeft:

    def findelement(self, nums: List[int]) -> List[int]:

        res = [-1] * len(nums)
        stack = []

        # for i in range(len(nums)-1,-1,-1):
        #     for j in range(i-1,-1,-1):
        #         if nums[i] < nums[j]:
        #             res[i]=nums[j]
        #             break
        # return res
        for i in range(len(nums)):
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(nums[i])
        return f"Next Greater Element to Left: {res}"


cl_obj = findGreaterElementLeft()
print(cl_obj.findelement(nums=[1, 3, 2, 4]))

'''Next Smaller Element to Left'''


class findSmallerElementLeft:
    def findelement1(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        # for i in range(len(nums)-1,-1,-1):
        #     for j in range(i-1,-1,-1):
        #         if nums[i] < nums[j]:
        #             res[i]=nums[j]
        #             break
        # return res
        for i in range(len(nums)):
            while stack and stack[-1] >= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(nums[i])
        return f"Next Smaller Element to Left: {res}"


cl_obj = findSmallerElementLeft()
print(cl_obj.findelement1(nums=[1, 3, 2, 4]))


class Parenthesis:
    def onlyoneparenthesis(self, s: str) -> bool:

        count = 0
        for chr in s:
            if chr == '(':
                count += 1
            elif chr == ')':
                count -= 1
        if count < 0:
            return f"parenthesis_check: False"

        return f"parenthesis_check: {count == 0}"


obj = Parenthesis()
print(obj.onlyoneparenthesis(s=')(())'))

'''Leetcode: Online Stock Span'''


# Soln: 1
class onlineStockSpan:
    def stockspan(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[i] < nums[j]:
                    res[i] = i - j
                    break
        return res


obj_st = onlineStockSpan()
print(obj_st.stockspan(nums=[100, 80, 60, 70, 60, 75, 85]))


# soln: 2 (optimized)

class onlineStockSpan:

    def __init__(self):
        self.stack = []

    def stockspan(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        for i in range(len(nums)):
            while self.stack and self.stack[-1][0] <= nums[i]:
                self.stack.pop()

            if self.stack:
                res[i] = i - self.stack[-1][1]

            self.stack.append((nums[i],i))

        return res


obj_st = onlineStockSpan()
print(obj_st.stockspan(nums=[100, 80, 60, 70, 60, 75, 85]))
