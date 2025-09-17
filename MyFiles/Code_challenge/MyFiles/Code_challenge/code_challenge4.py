"""
IF YOU INPUT A WRONG GENRE IT STOP THE PROGRAM BECAUSE YOU INPUT IS NOT VALID AND ALSO THE LENGTH AND DECADE
"""

print("Hello Welcome to the Manga Reader Recommender")
print("Answer a few question:")

genre = str(input("What genre that you type (action,romance,horror) --> ")).lower()
length = "How long this should manga be?(short,medium,long) -->"
decade = "What year?(2000,2024)-->"
#ACTION
if genre == "action":
    length = str(input(length)).lower()
    if length == "short":
        decade = eval(input(decade))
        if decade == 2000:
            print("WE RECOMMEND: Angel Sanctuary OVA 😇👼🔥😈 ")
        elif decade == 2024:
            print("WE RECOMMEND: Dandadan 👻👽⚡💥 ")
        else:
            print("The Year You Input is Not Available❌")
                     
    elif length == "medium":
        decade = eval(input(decade))
        if decade == 2000:
                print("WE RECOMMEND: Shaman King 🗡️👊🌀👻 ")
        elif decade == 2024:
            print("WE RECOMMEND: Go! Go! Loser Ranger! 🦸‍♂️🎭⚔️💥😈🎌 ")
        else:
            print("The Year You Input is Not Available❌")
        
    
    elif length == "long":
        decade = eval(input(decade))
        if decade == 2000:
           print("WE RECOMMEND: Naruto 🍥🔥🍃👊🌀")
        elif decade == 2024:
            print("WE RECOMMEND: ONE PIECE 🏴‍☠️☠️⚓🍖🌊👒")
        else:
            print("The Year You Input is Not Available❌")
        
    else:
        print("The Volume of Manga is Not Available❌")
        
#ROMANCE
elif genre == "romance":
    length = str(input(length)).lower()
    if length == "short":
        decade = eval(input(decade))
        if decade == 2000:
                print("WE RECOMMEND: Kareshi Kanojo no Jijou (Kare Kano) OVA🎭📖🏫😊💫")
        elif decade == 2024:
            print("WE RECOMMEND: Akira Failing in Love💘🏫🌸 ")
        else:
            print("The Year You Input is Not Available❌")
    
    elif length == "medium":
        decade = eval(input(decade))
        if decade == 2000:
            print("WE RECOMMEND: Mamotte Shugogetten🌙🧚‍♀️💖")
        elif decade == 2024:
            print("WE RECOMMEND: A Condition Called Love💞🌸💌")
        else:
            print("The Year You Input is Not Available❌")
    
    elif length == "long":
        decade = eval(input(decade))
        if decade == 2000:
            print("WE RECOMMEND: Peach Girl🍑💔👩‍🦰")
        elif decade == 2024:
            print("WE RECOMMEND: Pink & Habanero🌸💕")
        else:
            print("The Year You Input is Not Available❌")
    else:
        print("The Volume of Manga is Not Available❌")

#HORROR
elif genre == "horror":
    length = str(input(length)).lower()
    if length == "short":
        decade = eval(input(decade))
        if decade == 2000:
            print("WE RECOMMEND: Blood: The Last Vampire🩸🗡️👧🏻🦇🌑😱")
        elif decade == 2024:
            print("WE RECOMMEND: Toxic Daughter: Chi-chan🧪👧🩸")
        else:
            print("The Year You Input is Not Available❌") 
    elif length == "medium":
        decade = eval(input(decade))
        if decade == 2000:
            print("WE RECOMMEND: Hellsing🦇🔫🩸😈 ")
        elif decade == 2024:
            print("WE RECOMMEND: Parasyte: The Grey 🧑‍🤝‍🧑🦠")
        else:
            print("The Year You Input is Not Available❌")    
    
    elif length == "long":
        decade = eval(input(decade))
        if decade == 2000:
            print("WE RECOMMEND: Fushigi Yûgi: Genbu Kaiden 🗡️🩸🌌")
        elif decade == 2024:
            print("WE RECOMMEND: None identified🚫👻 ")
        else:
            print("The Year You Input is Not Available❌")
    else:
        print("The Volume of Manga is Not Available❌")
else:
    print("The Genre You Input is not available❌")
        


            
   