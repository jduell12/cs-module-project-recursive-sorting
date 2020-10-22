"""
Binary search

1. Find the midpoint element
    -round down if even elements
2. Compare the target agains the midpoint element
3. If the target matches the midpoint element return the index
4. Otherwise, determine which direction the binary search needs to go in
"""
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #base case - target not in the array
    if start > end:
        return -1
    else:
        #find midpoint 
        midpoint = (start + end) // 2
        #base case
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            #check the array from the midpoint + 1 to the end
            return binary_search(arr, target, (midpoint+1), end)
        else:
            #check the array from the start to the midpoint - 1
            return binary_search(arr, target, start, (midpoint -1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    #if sorted in ascending order
    if arr[0] < arr[len(arr)-1]:
        return binary_search(arr, target, 0, len(arr)-1)
    #sorted in descending order
    else:
       left = 0
       right = len(arr) - 1
       
       while left <= right:
           #find midpoint
           midpoint = (left + right) // 2
           #check if midpoint is the target value
           if arr[midpoint] == target:
               return midpoint
           elif arr[midpoint] < target:
               right = midpoint - 1
           else:
               left = midpoint + 1
       return -1
           
            
