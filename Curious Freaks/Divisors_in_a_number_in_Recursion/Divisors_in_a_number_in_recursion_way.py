
'''
RECURSION PROBLEM PRACTICE
Write a program to print the divisors of a number recursively.

Example:
Input: 6
Output: 1 2 3 6

Example:
Input: 12
Output: 1 2 3 4 6 12

'''


def divisors_in_recursion_way(n, i):

    if i > n:
        return 
    
    if n%i==0:
        print(i,end=' ')
    
    return divisors_in_recursion_way(n, i+1)


print('\nProgram Started...\n')

n = int(input('Enter a number : '))
divisors_in_recursion_way(n, 1)

print('\n\nProgram Ended...\n')