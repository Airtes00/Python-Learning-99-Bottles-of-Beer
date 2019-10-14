import sys

def bottles_song(beer):
    #Holding the lyrics in a dictionary to
    #take advantage of key value pairs.
    lyrics = {
        'v1':"bottles of beer on the wall!\n", #verse 1
        'v2':"bottles of beer!\n", #verse 2
        'v3':"take one down, pass it around!\n", #verse 3 
        'v1nos':"bottle of beer on the wall!\n",  #verse 1 without the s in bottles
        'v2nos':"bottle of beer!\n" #verse 2 without the s in bottles
        }
    for b in range(beer):
        if beer >= 2: #Do this if the value of beer is bigger or equal to 2
            print(str(beer),lyrics.get('v1'),str(beer),lyrics.get('v2'),lyrics.get('v3'))
            beer-=1
            if beer == 1: # checks to see if beer changed to 1 and uses verse 1 without the s
                print(str(beer),lyrics.get('v1nos'))  
            else:    
                print(str(beer),lyrics.get('v1'))# if it passes the check it prints as normal
                #bottles_song(beer) # same as the top. This is mostly me practicing recursion its probably not the best I know.
        else:
            print(str(beer),lyrics.get('v1nos'),str(beer),lyrics.get('v2nos'),lyrics.get('v3')) # final line for the last bottle
            beer-=1
            print(str(beer),lyrics.get('v1'))

beer = int(input(' How many beers do you have? and I will sing for each one! \n'))
bottles_song(beer)