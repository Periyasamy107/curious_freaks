

'''
Pattern Problem Practice

Sample 1:
Input:
n = 8

Expected output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 


Sample 2
Input:
n= 6

Expected output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 

'''


# PATTERN 14  

n = int(input('Enter a number to print a pattern : '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()

print('\nPattern 14 Completed\n')




'''
Pattern Problem Practice

Sample 1:
Input:
n = 2

Expected output:
1 
2 3


Sample 2
Input:
n= 5

Expected output:
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15

'''

# PATTERN 15

n = int(input('Enter a number to print a pattern : '))

count = 1 
for i in range(1, n+1):
    for j in range(1, i+1):
        print(count, end=' ')
        count += 1
    print()


print('\nPattern 15 completed\n')