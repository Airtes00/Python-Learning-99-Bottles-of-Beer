#Defined variables

beer = 99
verse1 = "bottles of beer on the wall\n\n"
verse2 = verse1[0:15] + "\n\n" #Prints only bottles of beer from verse 1
verse3 = "take one down, pass it around \n\n"
verse4 = verse1.replace("s", " ")# removes "S" from "beers"
verse5 = verse4[0:15] + "\n\n" #same as verse 2 but no "s"

if beer is not 0:
    while beer > 1:
        print(str(beer), verse1)
        print(str(beer), verse2)
        print(verse3)
        beer -= 1
        if beer is 1:
            print(str(beer), verse4)
        else:
            print(str(beer), verse1)
    else:
        print(str(beer), verse4)
        print(str(beer), verse5)
        print(verse3)
        beer -= 1
        print(str(beer), verse1)
