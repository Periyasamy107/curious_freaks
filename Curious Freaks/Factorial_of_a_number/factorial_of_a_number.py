
'''
MATHS PROBLEM:::::::::::


Write a program that gets n as input and print the factorial of a number(n!).

Testcase 1 :
Input : 
3

Expected output:
6


Testcase 2 :
Input : 
5

Expected output:
120


'''

print('Program Started....\n')

n = int(input('Enter a number : '))

fact = 1 
for i in range(1,n+1):
    fact *= i 

print(f'factorial of a number {n} is : {fact}')

print('\nProgram Ended....\n')