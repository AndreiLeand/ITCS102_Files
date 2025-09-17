"""
Create a program that prints the of a number entered by the user, using a simple for loop.

Ask the user to input a number.Use a for loop to print the multiplication table from for that number.Format each line clearly (e.g., 5 x 1 = 5).

 This reinforces:
Looping over a fixed range (range(1, 11))
Using the loop variable in calculations
String formatting
EXPECTED OUTPUT
MULTIPLICATION TABLE MAKER
Enter a number: 6

Multiplication table for 6:
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
"""

number = eval(input("Enter a number: "))
print("\nMultiplication table for",number,":")

for m in range(1,11):
    print(number,"x",m,"=",number * m)