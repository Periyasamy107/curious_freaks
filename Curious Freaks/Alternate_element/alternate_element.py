

'''
ARRAYS PROBLEM PRACTICE

You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

Examples:
Input: arr[] = [1, 2, 3, 4]

Output: 1 3

Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4


Input: arr[] = [1, 2, 3, 4, 5]

Output: 1 3 5

Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4
Take fifth element: 5


'''


def alternate_element(arr):

    n = len(arr)
    for i in range(1,n+1,2):
        print(i,end=' ')
    

print('\nProgram Started... \n')

arr = list(map(int, input('Enter the arr by space : ').split()))

print('Input array : ', arr)
print('Output : ',end='')
alternate_element(arr)

print()
print('\nProgram Ended...\n')
