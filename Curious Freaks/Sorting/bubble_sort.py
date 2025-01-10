
'''

BUBBLE SORT

time complexity ::::::::::
best case : O(n)
worst case : O(n^2)

space complexity ::::::::::
best case : O(1)
worst case : O(1)

'''


import random 

def bubble_sort(arr):

    n = len(arr)
    for i in range(n-1):
        swapped = False 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True 
        if not swapped:
            break
        
    return arr 


print('\nProgram started...\n')

arr = [random.randint(1,100) for _ in range(10)]
print(f'Unordered array : {arr}')
result = bubble_sort(arr)
print(f'Ordered array   : {result}')

print('\nProgram Ended...\n')
