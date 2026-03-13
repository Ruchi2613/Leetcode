from typing import List, Any


class next_smaller_element_to_left:
    def next_smaller_element(self,nums: List[int]) -> list[Any]:

        stack = []
        res = []

        for num in nums:
            if not stack:
                res.append(-1)
            elif num > stack[-1]:
                res.append(stack[-1])
            elif num <= stack[-1]:
                while stack and num <= stack[-1]:
                    stack.pop()
                if stack and num > stack[-1]:
                    res.append(stack[-1])
                else:
                    res.append(-1)
            stack.append(num)

        return res
cl = next_smaller_element_to_left()
print(cl.next_smaller_element(nums=[4,5,2,10,8]))