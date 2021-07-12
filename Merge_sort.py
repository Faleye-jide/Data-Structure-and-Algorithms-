"""
Merge sort is one of the most efficient sorting algorithm
in computer program. The intuition behind merge sort is based
on recursion and it does its operation in 0(nlogn) time.

Algorithm:
1. we need to check if its not an empty list - base case
2. otherwise we divide the array into two equal halves
3. using recursion, we are going to sort the two arrays given
a function
4. finally, we merge these two sorted array with another function
"""
# bruteforce approach 0(NlogN) time  and 0(N) space
nums = [21, 38, 29, 17, 4, 25, 32, 9]
def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    # sort the first half of the list
    left = mergeSort(left)

    # sort the second half of the list
    right = mergeSort(right)

    return mergeSortedlist(left, right)

def mergeSortedlist(left, right):
    sorted_list = []
    i = 0
    j = 0
    len_a = len(left)
    len_b = len(right)

    while i < len_a and j < len_b:
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len_a:
        sorted_list.append(left[i])
        i += 1

    while j < len_b:
        sorted_list.append(right[j])
        j += 1

    return sorted_list

print(mergeSort(nums))

# Efficient approach 0(NlogN), 0(1) time and space

def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # call recursion to sort the left half
    mergeSort(left)

    # call recursion to sort the right half
    mergeSort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums

print(mergeSort(nums))