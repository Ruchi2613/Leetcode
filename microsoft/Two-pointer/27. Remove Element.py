# class remove_ele:

#     def __init__(self, nums, val):
#         self.l = 0
#         self.r = len(nums)-1
#         self.nums = nums
#         self.val = val

#     def funcx(self):
#         while self.l <= self.r:
#             if self.nums[self.l] == self.val:
#                 self.nums[self.l],self.nums[self.r] = self.nums[self.r],self.nums[self.l]
#                 self.r -= 1
#             else:
#                 self.l += 1
#         return self.l 
    
# cl = remove_ele(nums=[0,1,2,2,3,0,4,2],val=2)
# print(cl.funcx())


class remove_ele:

    def funcx(self,nums,val):
        l = 0
        r = len(nums)-1

        while l <=r :
           
            if nums[l] == val:
               nums[l], nums[r] = nums[r],nums[l]
               r -=1
            else:
                l+=1
        return l 
           
cl = remove_ele()
print(cl.funcx(nums=[0,1,2,2,3,0,4,2],val=2))