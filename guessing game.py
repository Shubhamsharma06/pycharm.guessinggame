

import random
while(True):

    inp = int(input("Enter your Number \n"))
    # inp= random.randint(1,101)
    if inp >= 100:
        print("Congratulation you have entered a right Number")
        break
    else :
        print("Try again \n")
        continue