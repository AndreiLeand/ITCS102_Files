from activity24_1 import GreetPersonName,GreetInfo

# Creating or defining your own function
# Code reusability
# Keyword -- def


def GreetPerson():
    print("\nHi visitor, welcome to my first function")
    print("Please browse around")


GreetPersonName('Andrei')
GreetInfo('Andrei', 'Lucena', '20')


while True:
    print("Code compiler program")
    print("A - First Program \nB - Second Program \nC - Exit")
    choice = input("Select from the option -->").lower()

    if choice == 'a':
        GreetPersonName('Andrei')
        continue
    elif choice == 'b':
        GreetInfo('Andrei', 'Lucena', '20')
        continue
    elif choice == 'c':
        print("System Exit")
        break
    else:
        print("Invalid Choice")
        continue