class avg:

    def max_avg(self, nums, k):

        l = r = 0
        sum_num = 0
        avg_num = float('-inf')

        while r < len(nums):

            sum_num+=nums[r]

            if r-l+1 == k:
                avg_num = max(avg_num, sum_num/k)
                sum_num -= nums[l]
                l += 1
            r+=1
        return avg_num


cl = avg()
print(cl.max_avg(nums = [1,12,-5,-6,50,3], k = 4))