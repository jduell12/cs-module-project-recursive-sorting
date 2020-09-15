"""
Quicksort - O(n log n)
Divide-and-conquer method

1. Pick a pivot element (pick 1st array element)
2. Paritition the rest of the elements around the pivot element 
    - elements > pivot point will go in right partition
    - elements < pivot point will go in left partition 
3. Repeat until all elements are in a parition by themselves
4. Merge all the paritions into one array

Ex.
[15, 32, 126, 4, 7, 28, 96, 27, 52]
Pivot = 15 
[4, 7,][15][32, 126, 28, 96, 27, 52]
[4][7][15] [28, 27][32][126, 96, 52]
[4][7][15][27] [28][32] [96, 52][126]
[4][7][15][27] [28][32] [52][96][126]
[4, 7, 15, 27, 28, 32, 52, 96, 126]
"""
#helper function that picks the pivot and does the partitioning
def partition(arr):
    #initialize pivot element 
    pivot = arr[0]
    #initialize left and right partitions
    left = []
    right = []
    #iterate starting at index 1
    for x in range(len(arr)):
        if x != 0:
            if arr[x] <= pivot:
                left.append(arr[x])
            else:
                right.append(arr[x])
    #have elements partitions in the left, pivot and right arrays 
    return left, pivot, right 

def quick_sort(arr):
    #base case  - if length of arr is <= 1
    if len(arr) <= 1:
        return arr
    
    left, pivot, right = partition(arr)
    pivot = [pivot]
    qleft = quick_sort(left)
    qright = quick_sort(right)
    return qleft + pivot + qright
    
"""
Merge Sort - O(n log n)
Divide-and-Conquer method

1. Breaks array in half 
2. Keep breaking array in half until only 1 element in array
3. Merge arrays -> sorting them as you merge them

Ex.
[13, 27, 5, 18, 7, 3, 9, 22, 16, 56]
[13, 27, 5, 18, 7][3, 9, 22, 16, 56]
[13, 27, 5][18, 7][3, 9, 22][16, 56]
[13, 27][5][18][7][3, 9][22][16][56]
[13][27][5][18][7][3][9][22][16][56]
[13, 27][5, 18][3, 7][9, 22][16, 56]
[5, 13, 18, 27][3, 7, 9, 22][16, 56]
[3, 5, 7, 9, 13, 18, 22, 27][16, 56]
[3, 5, 7, 9, 13, 16, 18, 22, 27, 56]

 
"""

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    aLen = len(arrA)
    bLen = len(arrB)
    
    elements = aLen + bLen
    merged_arr = [0] * elements
    
    aIndex = 0
    bIndex = 0
    
    for i in range(len(merged_arr)):
        #check if at the end of the a arr
        if aIndex > aLen - 1:
            #since no more elements in a arr add rest of b arr elements
            merged_arr[i] = arrB[bIndex]
            bIndex += 1
        #check if at end of b arr
        elif bIndex > bLen - 1:
            #since no more lements in b arr add rest of a arr elements
            merged_arr[i] = arrA[aIndex]
            aIndex += 1
        #not at the end of either array
        else:
            if arrA[aIndex] > arrB[bIndex]:
                merged_arr[i] = arrB[bIndex]
                bIndex += 1
            else:
                merged_arr[i] = arrA[aIndex]
                aIndex += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #find middle value
    middle = len(arr) // 2
    
    #the left array holds all elements to the left of the middle value
    left = arr[:middle]
    
    #right array holds all elements to the right of that
    right = arr[middle:]    
    
    #if there's more than 1 number in the left array
    if len(left) > 1:
        left = merge_sort(left)
    
    #if there's more than 1 number in the right array
    if len(right) > 1:
        right = merge_sort(right)
    
    arr = merge(left, right)
    
    return arr
     
    
        
        
      

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

