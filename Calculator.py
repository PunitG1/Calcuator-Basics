import math
def Add(a, b):
    Answer = float(a) + float(b)
    return Answer

def Sub(a, b):
    Answer = float(a) - float(b)
    return Answer

def Divide(a, b):
    Answer = float(a) / float(b)
    return Answer

def Multiply(a,b):
    Answer = float(a) * float(b)
    return Answer

def Power(a, b):
#    if a.startswith("-"):
#    NegativeCheck = b % 2 
########################################## Next step is finding out how to deal with negative powers        
    Answer = math.pow(float(a), float(b))
    return Answer

# Above are the math functions to be called


def NextStep():
    FoundNextStep = False
    while FoundNextStep == False:
        ask2play = input("Do you need to calculate anything else? ( 'Y' or 'N' )")
        if ask2play.upper() == "Y":
            FoundNextStep = True
        elif ask2play.upper() == "N":
            FoundNextStep = True
            PlayAgain = False
            print("Have a nice day!")
        else:
            print("Sorry, invalid response.")
# Determines whether or not the user would like to re run the program to perform another calculation


def CheckINPUT(a, b, op):
    
    if (a).isnumeric() or (a.startswith("-") and a[1:].isnumeric()) or type(a) == float:
        print("First input accepted!")
        if b.isnumeric() or (b.startswith("-") and b[1:].isnumeric()) or type(b) == float:
            print("Second input accepted!")
            if op in ("+", "/", "-", "*", "^"):
                print("Operator accepted\n")
                return True
            else:
                print("Invalid operator entered. Please try again.")
                return False
        else:
            print("Input B is not valid, please ensure it is a numerical value")
            return False
    else:
        print("Input A is not valid, please ensure it is a numerical value")
        return False
#Determines whether the input received fits the criteria for the calculator.


def CalculatePrompt():
    ValidINPUT = False
    while ValidINPUT == False:
            
        INPUT1 = input ("Enter a number:")
        OPERATOR = input("Enter an operator:")
        INPUT2 = input("Enter a second number")
        Result = 0
        print("Checking your input...")
        ValidINPUT = CheckINPUT(INPUT1, INPUT2, OPERATOR)
                        
    else:
        
        if OPERATOR == "+":
            Result = Add(INPUT1, INPUT2)
        elif OPERATOR == "-":
            Result = Sub(INPUT1, INPUT2)
        elif OPERATOR == "/":
            Result = Divide(INPUT1, INPUT2)
        elif OPERATOR == "*":
            Result = Multiply(INPUT1, INPUT2)
        elif OPERATOR == "^":
            Result = Power(INPUT1, INPUT2)

        print(f"Calculated.", INPUT1, OPERATOR, INPUT2, " = ", Result, "\n")
        NextStep()
# User prompt and result displayed 




#Main Program call
PlayAgain = True
while PlayAgain:
    print("Hello. Welcome to the calculator program")
    CalculatePrompt()
        
