
# Problem Statement 1
'''Prob 1:
Write a program which takes two values x and y. Prints x for y number of times.

Input:
2 
3
Expected Output
2
2
2

Explanation - 2 is x and 3 is y in the input. So 2 is printed 3 times on the output.
'''

# Solution for the above problem statement 1
first_number = int(input('Enter a first number : '))
second_number = int(input('Enter a second number : '))
for i in range(second_number):
    print(first_number)




# Problem Statement 2
'''Prob 2:
Write a program to take x and print multiples of x till 1000.
Input:
100

Expected Output:
100
200
300
400
500
600
700
800
900
1000

Explanation - Input is 100, multiples of 100 is 100*1, 100*2, 100*3 and so on till 1000.
'''

# Solution for the above problem statement 2
number = int(input('Enter a number : '))
for i in range(1,11):
    print(number*i)




# Problem Statement 3
'''Prob 3:
Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.

Input
Nandy
Raja
3

Expected output:
NandyRaja
NandyRaja
NandyRaja

Explanation - Nandy is the firstName, Raja is the lastName and n is 5, so the expected output has NandyRaja printed 5 times.
'''

# Solution for the above problem statement 3
first_name = input('Enter a firstName : ')
last_name = input('Enter a lastName : ')
number = int(input('Enter a number : '))
for i in range(1,number+1):
    print(f'{first_name}{last_name}')

print('Testing')