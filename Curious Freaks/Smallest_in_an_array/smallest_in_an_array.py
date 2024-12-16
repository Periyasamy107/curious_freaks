
'''
ARRAY PROBLEM PRACTICE

Write a Program to find the smallest element in the Array
Input: 
n = 5

1 3 5 7 8

Ouput Expected:
1


Example 2
Input:
n = 8

5 7 34 67 2 56 5 8

Output:
2

'''

def find_smallest(inputs):

    small =inputs[0]
    for i in range(n):
        if inputs[i] < small:
            small = inputs[i]
    return small 


print('\nProgram Started...\n')


n = int(input('Enter a number : '))
inputs = list(map(int, input(f'Enter {n} elements with space : ').split()))

print(find_smallest(inputs))

print('\nProgram End......\n')

