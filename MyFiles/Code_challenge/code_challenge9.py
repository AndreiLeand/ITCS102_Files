"""
Create a fun program that acts like a parrot — it repeats anything the user says, using a for loop to "squawk" it back multiple times!

This challenge focuses purely on:
Using a simple for loop
Working with strings
Repeating an action without storing data
Ask the user to enter a phrase (e.g., "I love Python!").Ask how many times they want the parrot to repeat it.Use a for loop to print the phrase that many times.
Make each line sound like a parrot: " Squawk! {phrase}"   

Copy this bitmap image -> 

🦜

Expected output 🦜 PARROT SIMULATOR – THE ECHO CHAMBER!What do you want your parrot to say? I am hungry!
How many times should the parrot squawk it? 4

Listen to your parrot:
🦜 Squawk! I am hungry!
🦜 Squawk! I am hungry!
🦜 Squawk! I am hungry!
🦜 Squawk! I am hungry!
"""
say = str(input("What do you want your parrot to say?--> "))
repeat = eval(input("How many times should the parrot squawk it? --> "))

for p in range(repeat,0,-1):
   print("🦜 Squawk!",say)