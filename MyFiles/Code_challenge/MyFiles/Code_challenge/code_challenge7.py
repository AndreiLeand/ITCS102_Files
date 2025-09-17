"""
Simulate a simple countdown timer using a for loop that counts from a user-specified number down to 1, then prints "Liftoff! ".

Ask the user to enter a starting number (e.g., 5).Use a for loop to count from that number to 1.Print each number on a new line.After the loop ends, print "Liftoff! ".        

⏳ COUNTDOWN TIMER SIMULATOR
Enter the starting number for countdown: 5
Countdown started:
5
4
3
2
1
Liftoff!
"""

countdown = eval(input("Enter the starting number for countdown --> "))
for count in range(countdown,0,-1):
    print(count)
print("Liftoff!!")
