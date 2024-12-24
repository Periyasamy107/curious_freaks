
'''
ARRAYS PROBLEM PRACTICE 

Given an array arr, the task is to find whether the arr is palindrome or not. If the arr is palindrome then return true else return false.

An array is said to be palindrome if its reverse array matches the original array. 



Examples:

Input: arr = [1, 2, 3, 2, 1]
Output: true

Explanation: Here we can see we have [1, 2, 3, 2, 1] if we reverse it we can find [1, 2, 3, 2, 1] which is the same as before. So, the answer is true.


Input: arr = [1, 2, 3, 4, 5]
Output: false

Explanation: Here we can see we have [1, 2, 3, 4, 5] if we reverse it we find [5, 4, 3, 2, 1] which is the not same as before. So, the answer false.


'''

def is_palindrome(arr,n):

    i = 0 
    j = n-1
    while j>=i:
        if arr[i] != arr[j]:
            return False 
        if arr[i] == arr[j]:
            i += 1 
            j -= 1 
    return True 

print('\nProgram Started...\n')

arr = list(map(int, input('Enter the numbers with a comma (like this ,) : ').split(',')))
result = is_palindrome(arr,len(arr))
print(f'Output : {result}')

print('\nProgram Ended...\n')


        
