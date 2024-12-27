
'''
SIEVE OF ERATOSTHENES

Given a range [L, R]. The task is to find the sum of all the prime numbers in the given range from L to R both inclusive.

Examples:  

Input : L = 10, R = 20
Output : Sum = 60

Prime numbers between [10, 20] are:
11, 13, 17, 19
Therefore, sum = 11 + 13 + 17 + 19 = 60


Input : L = 15, R = 25
Output : Sum = 59

Note: Use sieve of eratosthenes to solve the problem

'''

import math 

def sieve_of_eratosthenes(L,R):

    arr = [0 for _ in range(R+1)]

    for i in range(2,int(math.sqrt(R)+1)):
        if arr[i] == 0:
            for j in range(i*i,R+1,i):
                arr[j] = 1 

    res = 0 
    for i in range(L,R+1):
        if arr[i] == 0:
            res += i 
    
    return res 


print('\nProgram Started...\n')

L = int(input('Starting Value : '))
R = int(input('Ending Value   : '))

answer = sieve_of_eratosthenes(L,R)
print(f'Output : {answer}')

print('\nProgram Ended...\n')