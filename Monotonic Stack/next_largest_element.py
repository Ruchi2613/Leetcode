from typing import List


class next_largest_element_to_right:
    def next_largest_element(self,nums: List[int]) -> int:

        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    ans.append(nums[i])
                    break
        ans.append(-1)
        return ans


cl = next_largest_element_to_right()
print(cl.next_largest_element(nums=[1, 3, 0, 0, 1, 2, 4]))