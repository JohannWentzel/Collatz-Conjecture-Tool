done = False
errorMsg = "Please enter a positive integer, or q to quit."

# Tutorial prints.
print("")
print("- - - - - - - - - - -")
print("COLLATZ CONJECTURE")
print("- - - - - - - - - - -")
print("")
print("Enter a positive integer to get its Collatz path,")
print("or enter q to quit.")

# Keep the tool looping until user quits.
while done == False:
    rawNum = raw_input("->  ")
    try:
        n = int(rawNum)
        if n <= 0:
            print(errorMsg)
        else:
            print(n)
            while (n != 1):
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = (3 * n) + 1
                print(n)

    # Catch non-string input.
    except ValueError as e:
        # User quits
        if rawNum == "q":
            print("Quitting...")
            done = True
        # User enters invalid input
        else:
            print(errorMsg)
