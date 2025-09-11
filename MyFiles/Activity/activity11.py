#ask user to input temperature outside 
#conditions as follow 
# 0 to negative temperature --- BELOW FREEZING 
# 1 to 15 - Extreme cold temperatures
# 16 to 30 - Cold Temp
# 31 to 38 - Lukewarm
# 39 to 42 - Warm Temperatures
# 43 to 50 - Hot temp
# 51 to 60 - Extremely Hot Temp
# 61 and above - Burning Temp

temp = input("Input Temperature --> ")
if int(temp.isnumeric()):
    if temp <= 0:
        print("Your temperature is Below Freezing")
    elif temp >=1 and temp <= 15:
        print("Your temperature is Extreme Cold")
    elif temp >= 16 and temp <= 30:
        print("Your temperature is Cold")
    elif temp >= 31 and temp <= 38:
        print("Your Temperature is Lukewarm")
    elif temp >= 39 and temp <= 42:
        print("Your temperature is Warm")
    elif temp >= 43 and temp <= 50:
        print("Your temperature is Hot temp")
    elif temp >= 51 and temp <= 60:
        print("Your temperature is Extremely Hot Temp")
    elif temp >= 61:
        print("Your temperature is Burning Temp")
else:
    print("Invalid Temp")
