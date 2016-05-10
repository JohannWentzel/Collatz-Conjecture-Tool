# - - - - - - - - - - -
#    COLLATZ.PY
#  Johann Wentzel
#   May 10, 2016
# - - - - - - - - - - -

import sys

def inputCheck( rawNum ):
    try:
        num = int(rawNum)
    # Catch non-string input.
    except ValueError as e:
        return False

    # Check for positive int.
    if num < 1:
        return False

    # Nothing has failed!
    return True



def main(argv):

    done = False
    errorMsg = "Please enter a positive integer, or q to quit."

    # Tutorial prints.
    print("")
    print("- - - - - - - - - - -")
    print("COLLATZ CONJECTURE")
    print("- - - - - - - - - - -")
    print("Enter a positive integer to get its Collatz path,")
    print("or enter q to quit.")

    # Keep the tool looping until user quits.
    while done == False:
        rawNum = raw_input("->  ")

        if rawNum == "q":
            # Quit if the user chooses to.
            print("Quitting...")
            done = True

        elif inputCheck(rawNum) == True:
            # Run the actual logic!
            n = int(rawNum)
            print(n)
            while (n != 1):
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = (3 * n) + 1
                print(n)

        else:
            # Something was entered wrong.
            print(errorMsg)
if __name__ == "__main__":
    main(sys.argv)
