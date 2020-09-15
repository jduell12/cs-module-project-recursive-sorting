"""
Quicksort - O(n^2)

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

"""
Merge Sort - O(n log n)

Divide-and-Conquer method
"""

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


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

