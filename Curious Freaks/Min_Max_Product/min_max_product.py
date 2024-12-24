
'''
ARRAYS PROBLEM PRACTICE 

Given two arrays of arr1 and arr2, the task is to calculate the product of the maximum element of the first array arr1, and minimum element of the second array arr2.

Examples :

Input : arr1 = [5, 7, 9, 3, 6, 2],  arr2 = [1, 2, 6, 1, 9]
Output : 9

Explanation: The max in arr1 is 9. The min element in arr2 is 1. The product is 9*1 = 9.


Input : arr1 = [0, 0, 0, 0],  arr2 = [1, 1, 2]
Output : 0

Explanation: The max in arr1 is 0. The min element in arr2 is 1. The product is 0*1 = 0.


'''

from random import randint

def min_max_productt(arr1, arr2):

    max1 = arr1[0]
    for i in arr1:
        if i > max1:
            max1 = i 

    min1 = arr2[0]
    for j in arr2:
        if j < min1:
            min1 = j

    result = max1 * min1

    return max1, min1, result 


print('\nProgram Started...\n')

arr1 = [randint(0,50) for _ in range(1,6)]

arr2 = [randint(0,50) for _ in range(1,11)]

max1, min1, result = min_max_productt(arr1, arr2)
print(f'Max from arr1 is : {max1}')
print(f'Min from arr2 is : {min1}')
print(f'Output : {result}')

print('\nProgram Ended...\n')