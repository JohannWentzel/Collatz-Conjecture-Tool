done = False

print("")
print("- - - - - - - - - - -")
print("COLLATZ CONJECTURE")
print("- - - - - - - - - - -")
print("")
print("Enter a positive integer to get its Collatz path,")
print("or press q to quit.")

while done == False:
    num = raw_input("->  ")
    if type(num) is int:
        
    elif type(num) is str and num == "q":
        done = True
    else:
        print("Please enter a positive integer.")
