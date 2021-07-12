"""
Selection sort is a simple sorting algorithm amd also an in-place comparison
steps to execute selection sort
1: search for the minimum element in a list
2. swap the element at the 0th index with the smallest value
3. the list has two parts; the sorted and unsorted then repeat 1 and 2 on the unsorted part till it is sorted

0(N^2) time complexity
0(1) extra space
"""
nums = [2, 9, 8, 7, 3, 5, 0]
def prob(nums):
    for i in range(len(nums)-1):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j

        temp = nums[i]
        nums[i] = nums[minIndex]
        nums[minIndex] = temp

    return nums

print(prob(nums))