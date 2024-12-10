
'''
MATHS PROBLEMS:::::::::::

Write a program that gets n as input and print the reverse of the number

Testcase 1 :
Input : 
325345

Expected output:
543523


Testcase 2 :
Input : 
987987

Expected output:
789789

'''


print('Program Started...\n')

n = int(input('Please enter a number : '))

reversed_number = 0 
temp = n

while temp > 0:

    last_digit = temp % 10
    reversed_number = ( reversed_number * 10 ) + last_digit
    temp //= 10 

print(f'Original number is : {n} and Reversed number is {reversed_number}')

print('\nProgram Ended....\n')
