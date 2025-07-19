class Solution:
    def relativeSortArray(self, arr1, arr2):

        #Solution 2:
        count = {}

        for num in arr1:
            if num not in count:
                count[num] = 0
            count[num] += 1
        print(count)

        result = []

        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]

        remaining_numbers = sorted(count.keys())
        for num in remaining_numbers:
            result.extend([num] * count[num])

        return result
cl = Solution()
print(cl.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))