

'''
Pattern Problem Practice 

Sample 1:
Input:
n = 4

Expected output:
4 3 2 1
3 2 1
2 1
1


Sample 2
Input:
n= 6

Expected output:
6 5 4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

'''

n = int(input('Enter a number to print the pattern : '))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

print('Program End')