list = []
print("Anime list maker")
while True:
    anime = input("Enter the title of an anime (Type 'exit' to finish): ")
    if anime.lower() == 'exit':
        print("Your exited about the anime entry program.")
        break
    
    list.append(anime)
entry = len(list)
print("Your anime list includes:")
for i in range(entry):
    print(f"- {list[i]}")
print("Good choice!")