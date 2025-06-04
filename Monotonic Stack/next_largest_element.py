from typing import List, Any


class next_largest_element_to_right:
    def next_largest_element(self,nums: List[int]) -> list[Any]:

        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             ans.append(nums[i])
        #             break
        # ans.append(-1)
        # return ans

        """if ever j is depended on i then it is a stack problem"""

        # stack = []
        # res = []
        # i = len(nums) - 1
        # while i >= 0:
        #     if not stack:
        #         res.append(-1)
        #     elif stack[-1] > nums[i]:
        #         res.append(stack[-1])
        #     elif stack[-1] <= nums[i]:
        #         stack.pop()
        #         continue
        #     stack.append(nums[i])
        #     i -= 1
        # return res[::-1]

        stack = []
        res = []
        for i in range(len(nums)-1, -1, -1):
            if not stack:
                res.append(-1)
            elif nums[i] < stack[-1]:
                res.append(stack[-1])
            elif nums[i] >= stack[-1]:
                while stack and nums[i] >= stack[-1]:
                    stack.pop()
                res.append(stack[-1])
            stack.append(nums[i])

        return res[::-1]

cl = next_largest_element_to_right()
print(cl.next_largest_element(nums=[1, 3, 0, 0, 1, 2, 4])) # [3, 4, 1, 1, 2, 4, -1]