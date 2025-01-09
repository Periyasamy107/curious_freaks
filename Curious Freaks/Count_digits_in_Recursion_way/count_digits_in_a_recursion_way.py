
'''
RECURSION PROBLEM PRACTICE

Write a recursive algorithm to find the count of digits in a number.

Example:
Input: 353445
Outpput: 6


Example 2 :
Input: 53543
Output: 5

'''

def count_digits_in_recursion_way(n):

    if n <= 0:
        return 0 
    else:
        return 1 + count_digits_in_recursion_way(n//10)
    

print('\nProgram Started...\n')

n = int(input('Enter a number : '))
answer = count_digits_in_recursion_way(n)
print(f'Number of digits in a given number is : {answer}')

print('\nProgram Ended...\n')


