
'''
ARRAYS PROBLEM PRACTICE 

Given an array arr of integers and an index key(0-based index). 
Your task is to return the element present at the index key in the array.

Input: key = 2 , arr = [10, 20, 30, 40, 50]
Output: 30

Explanation: The value of arr[2] is 30 .


Input: key = 4 , arr = [10, 20, 30, 40, 50, 60, 70]
Output: 50

Explanation: The value of the arr[4] is 50 .


'''


arr = [i*10 for i in range(1,11)]

def find_element(key,arr):

    n = len(arr)
    for idx in range(n):
        if key == idx:
            return arr[idx]
        
print('\nProgram Started...\n')

key = int(input('Enter the key to get the value : '))

value = find_element(key,arr)
print(f'Output : {value}')

print('\nProgram Ended...\n')
