import random

# Shit i use to make shit work

bullets = str([1, 2, 3, 4, 5, 6])
x = random.randint(1,6)
userInput = 0

#Experimental shit

game = True

# Shit that uses the shit that makes the shit work so the shit can work

while game == True:
    try:
        userInput = int(input("Choose a chamber between 1 and 6: "))
    except ValueError:
        print("You failed to choose a number...")
        print("")
        print("...")
        print("")
        print("...so your friend Bobita decides to unload the whole mag into your forehead.")
        print("")
        game = False
        conti = input("Want to play again? (Y/N) ")
        if conti == "Y":
            game = True
        else:
            game = False
            print("Farewell")
    else:
        input("Press enter to pull the trigger")
        print("")

        if userInput >= 7:
            print("You tried to shoot the 7th chamber of a 6 chamber gun...")
            print("")
            print("...")
            print("")
            print("...You failed so much your brain comited suicide.")
            print("")
            game = False
            conti = input("Want to play again? (Y/N) ")
            if conti == "Y":
                game = True
            else:
                game = False
                print("Farewell")

        elif x == userInput:
            print("Pow! You died.")
            print("")
            print("Deadly chamber: " +str(x))
            print("")
            print("Your choice: " +str(userInput))
            print("")
            game = False
            conti = input("Want to play again? (Y/N) ")
            if conti == "Y":
                game = True
            else:
                game = False
                print("Farewell")
        else:
            print("Click, you survived.")
            print("")
            print("Deadly chamber: " +str(x))
            print("")
            print("Your choice: " +str(userInput))
            print("")
            game = False
            conti = input("Want to play again? (Y/N) ")
            if conti == "Y":
                game = True
            else:
                game = False
                print("Farewell")
