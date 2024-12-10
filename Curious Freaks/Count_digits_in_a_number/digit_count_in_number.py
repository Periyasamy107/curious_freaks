
'''
MATHS PROBLEM:::::::::::

Write a program that gets n as input and print the number of digits in the number

Testcase 1 :
Input : 
325345

Expected output:
6

Testcase 2 :
Input : 
9879

Expected output:
4

'''

print('Program Started...\n')

n = int(input('Enter a number : '))

count = 0 

while n > 0:
    count += 1 
    n = n // 10 

print('Number of digits in the number is : ', count)
print('\nProgram Ended...\n')