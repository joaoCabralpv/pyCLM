class Inside:
    pass

# Creates a simple menu in the style:
#foo1 bar
#foo2 test
#foo3 word

def menu(choises , *, index="", indexStart=1, Input=False, functions=[],functionIndexStart=None):
    #loops trough the choises
    if functionIndexStart==None:
        functionIndexStart=indexStart
    for i in range(len(choises)):
        if index:
            #Adds the index to the choise. $Number is replaced with the number of the index startig at indexSart
            print(index.replace("$Number",str(i+indexStart)) + choises[i])
        else:
            print(choises[i])
    if Input:
        InputResult=input()
        if not InputResult.isnumeric():
            #Makes so that the functions arent called, avoinding a crash
            functions=False
        if functions:
            functions[int(InputResult)-functionIndexStart]()
            return InputResult


