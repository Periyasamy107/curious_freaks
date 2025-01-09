

'''
RECURSION PROBLEM PRACTICE
Write a Program to find the power of a number recursively. Take two inputs, number and the power.

Example:
Input: 2 3
Output: 8

Explanation : 2^3 is 8

Example:
Input: 5 2
Output: 25

Explanation: 5^2 is 25


'''


def power_of_a_number_recursion(b,p):

    if p == 0:
        return 1 
    
    return b * power_of_a_number_recursion(b, p-1)


print('\nProgram Started...\n')

inputs = list(map(int, input('Enter two numbers as base and power : ').split()))
base = inputs[0]
power = inputs[1]
result = power_of_a_number_recursion(base, power)
print(f'Power of a given number is : {result}')

print('\nProgram Ended...\n')