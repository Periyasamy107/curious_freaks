
'''
MATHS PROBLEMS::::::::::::::

PRIME NUMBER>>>>>>>>

Write a program that gets n as input and print all the prime numbers till that number.
Testcase 1 :
Input : 
5

Expected output:
2 3 5


Testcase 2 :
Input : 
11

Expected output:
2 3 5 7 11

'''


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False 
    return True 

temp = []

def prime_numbers(number):
    for i in range(2, number+1):
        if is_prime(i):
            temp.append(i)

print('\nProgram Started....\n')

n = int(input('Enter a number : '))

prime_numbers(n)

print(f'\nPrime numbers for a given number range : {temp}\n')

print('Program Ended...')

