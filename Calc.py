#SETUP
import os
print("Please wait")
#make a new command called palc()
def Calc():
    while True:
        print()
        print("Welcome to Palc!")
        print()
#CALCULATION CHOICE
        calc = input("Calculation?  (type ? for help): ")
#HELP
        if calc == "?":
            print('''
            Currently supported: multiplication (*), division (/), addition (+), square (sq), subtraction (-), modulo (%), area (#), volume (vol), cube ({}), and cube twice ({2}). Type exit to exit. Commands are case-sensitive
            To access support: go to https://github.com/thetechrobo/support/
            To modify Palc: go to https://github.com/thetechrobo/python-text-calculator/
            ''')
#MULTIPLICATION
        elif calc == "*":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 * number2)
            print()
            
        elif calc == "x":
            print()
            number1 = int(input("First number? "))
            number2 = int(input("Second number? "))
            print()
            print(number1 * number2)
            print()
#SQUARE
        elif calc == "sq":
            print()
            squaredNumber = int(input("Type the number to be squared: "))
            print()
            print(squaredNumber * squaredNumber)
            print()
        elif calc == "[]":
            print()
            squaredNumber = int(input("Type the number to be squared: "))
            print()
            print(squaredNumber * squaredNumber)
            print()
#DIVISION
        elif calc == "/":
            print()
            number1 = int(input("type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 / number2)
            print()
        elif calc == "div":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 / number2)
            print()
#SUBTRACTION
        elif calc == "-":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("type the second number: "))
            print()
            print(number1 - number2)
            print()
        elif calc == "sub":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("type the second number: "))
            print()
            print(number1 - number2)
            print()
        elif calc == "min":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("type the second number: "))
            print()
            print(number1 - number2)
            print()
#ADDITION
        elif calc == "+":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 + number2)
            print()
        elif calc == "add":
            print()
            number1 = int(input("Type the first number: "))
            number2 = int(input("Type the second number: "))
            print()
            print(number1 + number2)
            print()
#MODULO
        elif calc == "%":
            print()
            try:
                number1 = int(input("Type the first number(greater): "))
                number2 = int(input("Type the second number(smaller): "))
            except (TypeError, ValueError):
                print("Error!")
                print("Invalid input (code 1)")
                print()
            if(abs(number1)<abs(number2)):
                print()
                print("Error!")
                print("The second number entered is greater than the first number")
                print()
                Calc()
            else: 
                print(number1-number2*int(number1/number2))
                print()
        elif calc == "mod":
            print()
            try:
                number1 = int(input("Type the first number(greater): "))
                number2 = int(input("Type the second number(smaller): "))
            except (TypeError, ValueError):
                print("Error!")
                print("Invalid input (code 1)")
                print()
            if(abs(number1)<abs(number2)):
                print()
                print("Error!")
                print("The second number entered is greater than the first number")
                print()
            else: 
                print(number1-number2*int(number1/number2))
                print()
#AREA        
        elif calc == "ar":
            win = input("Is your OS the following: Windows? (Y/n, case-sensitive)")
            if win == "Y":
                print()
                os.system(start python area.py)
            else: 
                print()
                print("Mac or Linux, I assume, then")
                os.system('python3 area.py')
                print()
        elif calc == "#":
            win = input("Is your OS the following: Windows? (Y/n, case-sensitive)")
            if win == "Y":
                print()
                os.system(start python area.py)
            else: 
                print()
                print("Mac or Linux, I assume, then")
                os.system('python3 area.py')
                print()
#VOLUME
        elif calc == "vol":
            win = input("Is your OS the following: Windows? (Y/n, case-sensitive)")
            if win == "y":
                print()
                os.run(start python volume.py)
            else: 
                print()
                print("Then we're going to assume Mac or Linux.")
                os.system('python3 volume.py')
                print()
#CUBE
        elif calc == "{}":
            print()
            cubedNumber = int(input("Type the number to be cubed: "))
            print()
            print(cubedNumber * cubedNumber * cubedNumber)
            print()
        elif calc == "exit":
            exit()
#CUBE TWICE
        elif calc == "{2}":
            print()
            cubedNumber = int(input("Number?"))
            print()
            print(cubedNumber * cubedNumber * cubedNumber * cubedNumber * cubedNumber * cubedNumber)
        else:
            print('''
            print("I don't understand your request. Here are the currently supported calculations: * or x; / or div; -, min, or sub; + or add; % or mod (modulo); sq or [] (square); ar or # (area); vol (volume); {} (cube); and {2} (cube twice). Sorry for the inconvenience")
            ''')

print()
Calc() #run the Calc() command above
