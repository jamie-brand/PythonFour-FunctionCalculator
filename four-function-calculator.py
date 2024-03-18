# Four-function calculator program.

# Define function to request first number.
def request_number_1():
    number_1 = None
    while number_1 == None:
        try:
            number_1 = float(input("""\nEnter the first number: """))
        except ValueError:
            print("""You must enter a number. Please try again.""")
            number_1 = None
        except Exception as err:
            print("""Error:""", err)
    return float(number_1)


# Define function to request second number.
def request_number_2():
    number_2 = None
    while number_2 == None:
        try:
            number_2 = float(input("""\nEnter the second number: """))
        except ValueError:
            print("""You must enter a number. Please try again.""")
            number_2 = None
        except Exception as err:
            print("""Error:""", err)
    return float(number_2)


# Define addition function.
def addition(number_1, number_2):
    added = number_1 + number_2
    print(f"""\nAdding {number_1} and {number_2} equals {added}.""")


# Define subtraction function.
def subtraction(number_1, number_2):
    subtracted = number_1 - number_2
    print(f"""\nSubtracting {number_1} and {number_2} equals {subtracted}.""")


# Define multiplication function.
def multiplication(number_1, number_2):
    multiplied = number_1 * number_2
    print(f"""\nMultiplying {number_1} and {number_2} equals {multiplied}.""")


# Define division function.
def division(number_1, number_2):
    # If the second number is zero, print error.
    if number_2 == 0:
        print("""\nYou can't divide by zero. Please start over. \n""")
        # Instead of ending the program, restart from the beginning.
        main()
    else:
        divided = number_1 / number_2
        print(f"""\nDividing {number_1} and {number_2} equals {divided}.""")


# Define the menu function.
def menu():
    # Print the menu.
    print("""\nCalculations:""", """  1. Addition""", """  2. Subtraction""", """  3. Multiplication""", """  4. Division""", sep="\n")

    # Ask the user to select the calculation from the menu.
    menu_choice = input("""\nWhich calculation would you like to perform? (Press any key other than "1", "2", "3", or "4" to quit the program.) """)
    try:
        if menu_choice == "1":
            # Call the functions to request the numbers.
            number_1 = request_number_1()
            number_2 = request_number_2()
            # Call the function to add the numbers.
            addition(number_1, number_2)
        elif menu_choice == "2":
            # Call the functions to request the numbers.
            number_1 = request_number_1()
            number_2 = request_number_2()
            # Call the function to subtract the numbers.
            subtraction(number_1, number_2)
        elif menu_choice == "3":
            # Call the functions to request the numbers.
            number_1 = request_number_1()
            number_2 = request_number_2()
            # Call the function to multiply the numbers.
            multiplication(number_1, number_2)
        elif menu_choice == "4":
            # Call the functions to request the numbers.
            number_1 = request_number_1()
            number_2 = request_number_2()
            # Call the function to divide the numbers.
            division(number_1, number_2)
        else:
            print("""\nThank you for using this program. Goodbye.""")
    except Exception as err:
        print("""Error:""", err)


# Define the function to restart the program / run a new calculation.
def restart():
    # Ask the user whether to run a new calculation.
    restart_choice = None
    while restart_choice == None:
        restart_choice = input("""\nWould you like to perform a new calculation? (Press "y" or "1" to continue. Press any other key to quit the program.) """)
        try:
            if restart_choice == "y" or restart_choice == "Y" or restart_choice == "1":
                # Call the menu function and then call the restart function.
                menu()
                restart()
            else:
                print("""\nThank you for using this program. Goodbye.""")
        except Exception as err:
            print("""Error:""", err)


# Define the main function.
def main():
    print("""This program performs basic calculations with two numbers for you.""")

    # Call the menu function.
    menu()

    # Call the restart function.
    restart()


# Call the main function.
main()