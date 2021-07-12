nums = [7,8,2,0,9,5,3]
def sort(nums):
   for i in range(len(nums)-1):
       for j in range(len(nums)-1):
           if nums[j] < nums[j+1]:
               continue
           temp = nums[j]
           nums[j] = nums[j+1]
           nums[j+1] = temp

   return nums
print("sorted_nums:" ,sort(nums))