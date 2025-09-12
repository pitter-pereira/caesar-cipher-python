import string
import cc_functions as cc

action = input("Would you like to encrypt (1) or decrypt(2)?: ")

message = input("\nEnter the message: ")

if (action != "1" and action != "2"):

    print("Action not supported")

elif (action == "1"):

    number =  input("You want to encrypt. Enter the number of jumps: ")

    cc.encrypt(message, number)

else:
    
    number =  input("You want to encrypt. Enter the number of jumps: ")

    cc.decrypt(message, number)