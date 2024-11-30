
# Problem Statement 1
'''Write a program that takes an integer, then a string, then a char from the user and prints them in the screen.

Input:  2 Name y

Expected Output:
2
Name
y
'''

# Solution for the above problem statement 1
user_input = input("Enter a details: ").split()
print(int(user_input[0]))
print(user_input[1])
print(user_input[2])







# Problem Statement 2
'''Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.

If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.

Input: 45 45 45

Expected Output: 

Triangle cannot be formed

Explanation -> We are getting 3 inputs, that is three angles of triangle, but here the sum of three angles that is 45+45+45 is not equal to 180 so Triangle cannot be formed is the output.
'''

# Solution for the above problem statement 2
user_input = list(map(int,input("Enter a values for the angles: ").split()))

total = 0 
for value in user_input:
    total += int(value)

print('triangle can be formed' if total==180 else "triangle cannot be formed")









# Problem Statement 3
'''Prob 3: 
Given mark of student, Print the Grade
Grade A if mark is greater than or equal to 90
Grade B if mark is greater than or equal to 80
Grade C if mark if greater than or equal to 60
Grade D if mark if greaer than or equal to 35
Fail if mark is lesser than 35

Input: 95
Expected Output:
Grade A

Explanation: Here 95 is greater than or equal to 90 so its Grade A
'''

# Solution for the above problem statement 3
mark = int(input('Please enter the mark : '))
if mark >= 90:
    print('Grade A')
elif mark >= 80:
    print('Grade B')
elif mark >= 60:
    print('Grade C')
elif mark >= 35:
    print('Grade D')
else:
    print('Fail')




# Problem Statement 4
'''Prob 4: Write a program using switch case which takes a value and prints the respective Size.

If size is 29 then its small
If size is 30 then its Medium
If size is 38 then its Large
If size is 42 then its XLarge
If size is not any of the above then Invalid.

Input: 29
Expected Output: 
Small
'''

# Solution for the above problem statement 4
# This code runs only in python 3.10 or above versions
def size_validator(argument):
    if argument == 29:
        return 'Small'
    elif argument == 30:
        return 'Medium'
    elif argument == 38:
        return 'Large'
    elif argument == 42:
        return 'XLarge'
    else:
        return 'Invalid'
 

value = int(input('Enter a value : '))
print(size_validator(value))


