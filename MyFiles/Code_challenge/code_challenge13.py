name = input("Input your name --> ")
print("------------------------------------")
print("ODD NUMBER SUMMATION,press 0 to stop")
print("------------------------------------")

number = 0
sum = 0
odd = ""

while number == 0:
    
    input_num = int(input("Input any number --> "))

    if input_num % 2 == 1:
        sum += input_num
        odd += str(input_num) + " "
        print("ODD NUMBER DETECTED,code continues")
        continue
    
    elif input_num == 0:
        print(f"Program stops.!!!\nHi {name},the sum of all ODD number is {sum}")
        print("ODD numbers detected included : ",odd)
        break
    else:
        if int(input_num % 2 == 0):
            print("EVEN NUMBER DETECTED,code continues")
            continue
        else:
            print("Invalid input")