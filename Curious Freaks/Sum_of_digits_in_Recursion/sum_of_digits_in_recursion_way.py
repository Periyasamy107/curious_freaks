
'''
RECURSION PROBLEM PRACTICE 
Write a recursive program to find the sum of digits of a number.

Example 1:
Input: 342
Output: 9

Example 2:
Input: 34534
Ouput: 19

'''

def sum_of_digits_in_recursion_way(n):

    if n <= 0:
        return 0 
    
    return (n%10) + sum_of_digits_in_recursion_way(n//10)


print('\nProgram Started...\n')

n = int(input('Enter a number : '))
result = sum_of_digits_in_recursion_way(n)
print(f'Sum of a digits in a given number : {result}')

print('\nProgram Ended...\n')