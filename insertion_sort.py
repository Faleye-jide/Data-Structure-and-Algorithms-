nums = [2, 9, 8, 7, 3, 5, 0]

def insertionSort(nums):
   for i in range(len(nums)):
       cur_ele = nums[i]
       pos = i

       while pos > 0 and cur_ele < nums[pos-1]:
           nums[pos] = nums[pos-1]
           pos-=1
       nums[pos] = cur_ele

   return nums
print(insertionSort(nums))












