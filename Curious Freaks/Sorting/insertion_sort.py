


'''

INSERTION SORT

time complexity ::::::::::
best case : O(n)
worst case : O(n^2)

space complexity ::::::::::
best case : O(1)
worst case : O(1)

'''


import random 


# METHOD 1 ::::::
def insertion_sort(arr):
    for i in range(1,len(arr)):

        insert_idx = i 
        current_value = arr.pop(i)

        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_idx = j 

        arr.insert(insert_idx, current_value)

    return arr


# # METHOD 2 ::::::
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]

#         j = i - 1 
#         while j>=0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1 

#         arr[j+1] = key 

#     return arr


print('\nProgram started...\n')

arr = [random.randint(1,100) for _ in range(5)]
print(f'Unordered array : {arr}')
result = insertion_sort(arr)
print(f'Ordered array   : {result}')

print('\nProgram Ended...\n')
