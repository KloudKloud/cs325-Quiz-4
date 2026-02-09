def menu():

    print("===================================\n")
    print("For addition, type \"1\"")
    print("For subtraction, type \"2\"")
    ## print("For multiplication, type \"3")
    ## print("For division, type \"4\"")
    print("To exit the program, type \"3\"")
    print("\n===================================")

def prompt():

    choice = int(input("Enter your choice: "))

    while choice != 3:

        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        ## elif choice == 3:
            ## multiply()
        ## elif choice == 4:
            ## divide()
        else:
            print("Incorrect entry. Please try again: ")

        menu()
        choice = int(input("Enter your choice: "))


def adding():

    num1 = int(input("Enter your first number to add: "))
    num2 = int(input("Enter your second number to add: "))

    result = num1 + num2

    print("Your result is: " + str(result))

def subtraction():

    num1 = int(input("Enter your first number to subtract: "))
    num2 = int(input("Enter your second number to subtract: "))

    result = num1 - num2

    print("Your result is: " + str(result))

##def multiply():
##
##    num1 = int(input("Enter your first number to multiply: "))
##    num2 = int(input("Enter your second number to multiply: "))

##    result = num1 * num2

##    print("Your result is: " + str(result))

##def divide():

##    num1 = int(input("Enter your first number to divide: "))
##    num2 = int(input("Enter your second number to divide: "))

##    result = num1 / num2

##    print("Your result is: " + str(result))

def exit():
    
    print("Have a great one!")

def main():

    menu()
    prompt()
    exit()



if __name__ == "__main__":
    main()