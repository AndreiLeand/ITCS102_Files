#ODD NUMBER SUMMATION
#ENTER 7 RANDOM NUMBERS, GET THE SUMMATION OF ALL ODD NUMBERS GIVEN
"""
enter a number: 10
enter a number: 4
enter a number 3
enter a number: 11
enter a number : 84
enter a number : 7
enter a number : 1

The summation of odd number = 22

"""

sum = 0

for odd in range(1,8,1):
    number = eval(input("Input any number --> "))
    if number % 2:
     sum += number
print("The summation of all odd numbers is =",sum)