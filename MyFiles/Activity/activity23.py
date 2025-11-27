snack1 = "Turon"
snack2 = "Lumpia"
#List with default values

snack = ['Turon', 'Lumpia', 'Bananaque', 'Habhab', 'Shanghai', 'Kamoteque', 'Karyoka']
            #0        1          2           3          4            5           6
print(snack)

#Every list has an index value / address
print(snack[3])
print(snack[2 : 5]) #List slicing

#Appending or adding items on the end of the list
snack.append("Maruya")
print(snack)

snack.append("Binangkal")
print(snack)

#Inserts item at specified index
snack.insert(4, "Palitaw")
print(snack)

#Remove first occurence of item
snack.remove("Turon")
print(snack)

#Removes and returns item at index
snack.pop()
print(snack)

#Returns number of elements
print(len(snack))


#Sorts the list(ascending by default)
snack.sort()
print(snack)

#Reverses the list order
snack.reverse()
print(snack)