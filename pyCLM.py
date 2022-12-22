class Inside:
    pass

# Creates a simple menu in the style:
#foo1 bar
#foo2 test
#foo3 word

def menu(choises , *, index="", indexStart=1, Input=False):
    #loops trough the choises
    for i in range(len(choises)):
        if index:
            #Adds the index to the choise. $Number is replaced with the number of the index startig at indexSart
            print(index.replace("$Number",str(i+indexStart)) + choises[i])
        else:
            print(choises)
    if Input:
        return input()
