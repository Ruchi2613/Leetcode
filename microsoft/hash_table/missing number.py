def missingNumber(self, nums) -> int:
    
        n = len(nums)

        i = 0
        while i < n:
            correct_index = nums[i]
            if nums[i] < n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # Find the missing number
        for i in range(n):
            if nums[i] != i:
                return i

        return n

