'''
Pattern Problem Practice

Sample 1:

Input:
n = 4

Expected output:
*
* *
* * *
* * * *


Sample 2
Input:
n= 6

Expected output:
*
* *
* * *
* * * *
* * * * *
* * * * * *

'''


n = int(input('Please enter a number to print the pattern : '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()


print(f'\nProgram End\n')