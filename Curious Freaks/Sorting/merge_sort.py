


'''

MERGE SORT

time complexity ::::::::::
worst case : O(n log n)

space complexity ::::::::::
worst case : O(n)

'''


import random 


# METHOD 1 ::::::
def merge_sort(arr):

    if len(arr) > 1:

        left_arr = arr[ 0 : len(arr)//2 ]
        right_arr = arr[ len(arr)//2 : len(arr) ]

        merge_sort(left_arr)
        merge_sort(right_arr)

        merge(left_arr, right_arr, arr)

def merge(left_arr, right_arr, arr):
    i = j = k = 0 

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1 

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1 
        k += 1 



print('\nProgram started...\n')

arr = [random.randint(1,100) for _ in range(5)]
print(f'Unordered array : {arr}')
merge_sort(arr)
print(f'Ordered array   : {arr}')

print('\nProgram Ended...\n')





# # METHOD 2 ::::::
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr 
    
#     left_arr = arr[ : len(arr)//2 ]
#     right_arr = arr[ len(arr)//2 : ]

#     left_sorted = mergeSort(left_arr)
#     right_sorted = mergeSort(right_arr)

#     return merging(left_sorted, right_sorted)

# def merging(left_sorted, right_sorted):

#     merged = []
#     i = j = 0

#     while i < len(left_sorted) and j < len(right_sorted):
#         if left_sorted[i] <= right_sorted[j]:
#             merged.append(left_sorted[i])
#             i += 1
#         else:
#             merged.append(right_sorted[j])
#             j += 1

#     merged.extend(left_sorted[i:])
#     merged.extend(right_sorted[j:])

#     return merged 


# print('\nProgram started...\n')

# arr = [random.randint(1,100) for _ in range(5)]
# print(f'Unordered array : {arr}')
# result = mergeSort(arr)
# print(f'Ordered array   : {result}')

# print('\nProgram Ended...\n')