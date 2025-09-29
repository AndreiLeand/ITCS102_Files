#start - optional value/parameter - default 0
#stop - required parameter / value
#step - optional value / parameter - default 1


for i in range(1,11,1):
    for x in range(1,i,1):
        print("🌚",end=" ")
    for y in range(10,i,-1):
        print("🌞",end=" ")
    print()