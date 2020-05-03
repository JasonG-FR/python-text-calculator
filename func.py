def logger(tolog):
    loggerontis = open ("palc.log", "a+")
    loggerontis.write(tolog)
def getNum(): #ask for two numbers and then return to function
    n1 = int(input("Please enter the first number: "))
    n2 = int(input("Please enter the second number: "))
    logger(("Palc got two numbers: ", n1, ", and ", n2))
    return n1, n2
def help():
    print('''
     Current list of commands: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), cube twice ({2}), exponents (ex), root (root), equals (=), logarithm (log), and convert number systems (base). Type exit to exit.
     Bugs? Head on over to https://github.com/thetechrobo/support/
     To contribute: go to https://github.com/thetechrobo/python-text-calculator/
     ''')
def multi(): #multiplication
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 * n2)
    logger(("User multiplied ", n1, " by ", n2, " and got result ", (n1 * n2)))
def div(): #division
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 / n2)
    logger(("User divided ", n1, " by ", n2, ", getting a result of ", (n1 / n2)))
def sub(): #subtraction
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 - n2)
    logger(("User subtracted ", n1, " to ", n2, " and got result ", (n1 - n2)))
def add(): #addition
    n1, n2 = getNum()
    print("\nThat equals...")
    print(n1 + n2)
    logger(("User added ", n1, " to ", n2, " and got result ", (n1 + n2)))
def mod(): #modulo
    try:
        bigger = int(input("\nType the first number (greater): "))
        smaller = int(input("Type the second number (smaller): "))
    except (TypeError, ValueError):
        print("\nError!")
        print("Invalid input (code 1)\n")
        logger(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 1."))
    if(abs(bigger)<abs(smaller)):
        print("\nError!")
        print("The second number entered is greater than the first number (code 2)\n")
        logger(("ERROR: attempted to modulo numbers ", bigger, " and ", smaller, ", but errored code 2."))
    else:
        print("\nThat equals...")
        print(bigger-smaller*int(bigger/smaller))
        logger(("User attempted to modulo numbers ", bigger, " and ", smaller, ", and got result ", (bigger-smaller*int(bigger/smaller))))
        print()
def base():
    base = int(input('''What base would you like to use?
    Available: 2 (binary) 8 (octo) 10 (decimal (normal)) 16 (hex)
    Type 2, 8, 10, or 16: '''))
    if base == 2:
        result = bin(int(input("Type the original number: "))) #bin() the number
        printThis = "=" +str(result)
        logger(("User binaried number ", result, ", getting a result of ", printThis))
        print(printThis)
    elif base == 8:
            result = oct(int(input("Type the original number: "))) #oct() the number
            printThis = "=" +str(result)
            logger(("User oct'ed number ", result, ", getting a result of ", printThis))
            print(printThis)
    elif base == 10:
        goodanswer = False
        while goodanswer is False:
            whichType = input("Which type is the Number (ord, binary, octo, or hex): ")
            if whichType == "ord":
                goodanswer = True
                result = int(ord(input("Type the original number: "))) #int() the number
            elif whichType == "binary":
                goodanswer = True
                result = int(bin(input("Type the original number: "))) #int() the number
            elif whichType == "octo":
                goodanswer = True
                result = int(oct(input("Type the original number: "))) #int() the number
            elif whichType == "hex":
                goodanswer = True
                result = int(hex(input("Type the original number: "))) #int() the number
            else:
                print("That was an invalid answer. Try again.")
            printThis = "=" +str(result)
            logger(("User int'ed number ", result, ", getting a result of ", printThis))
            print(printThis)
    elif base == 16:
        result = hex(int(input("Type the original number: "))) #ask for original number
        printThis = "=" +str(result)
        logger(("User hexed number ", result, ", getting a result of ", printThis))
        print(printThis)
def uc():
    import runpy
    logger(("User ran `volume.py'. Log is currently unavailable for area and volume."))
    runpy.run_path(path_name='volInteractive.py')
def area():
    import runpy
    logger(("User ran `area.py'. Log is currently unavailable for area and volume."))
    runpy.run_path(path_name='areaInteractive.py')
def log(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
    import math
    while True:
        base = input("What base would you like to use? \nCurrentlysupported: 10 (base 10), e (natural)")
        if base == "10":
            print("Using base 10")
            number = int(input("What is the number? "))
            print(math.log10(number))
            logger(("User used base 10 logarithm with number", number, ", getting a result of ", math.log10(number)))
            break
        elif base.lower() == "e":
            print("Using natural logarithm")
            number = int(input("What is the number? "))
            print(math.log(number))
            logger(("User used natural logarithm with number ", number, ", getting a result of ", math.log(number)))
            break
        else:
            print("The logarithm you typed is not available.")
            print("Try again.")
            logger(("User attempted to use a logarithm that is unavailable."))
def remember():
    print("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor.")
    toRemember = float(input("\nPlease enter the number to be saved: "))
    toRemember = str(toRemember)
    memory = open("memory", "w+")
    memory.write(toRemember)
    logger(("Saved number ", toRemember, " to file `memory'"))
def readMyMemory():
    print("This is the remember function.\nIt will read a number that was previously stored in a file.")
    try:
        memory = open("memory", "r")
        print("Number: ", memory.read())
        logger(("Retrieved number ", memory.read(), " from memory."))
    except:
        logger("There was an error retrieving the file from memory.")
        print("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file?")