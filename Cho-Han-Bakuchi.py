from random import *
cash_total = 100 
name = input("Please Enter a Username: ")
print("Hello " + name.title() +"!\n")
print("Let's Play a Game of Cho-Han! ")
print("Available cash winnings: " + "$", cash_total)
def cho_han(): 
    global cash_total 
    odd_or_even = str(input("Please enter odd or even: "))
    if odd_or_even.lower() == "even" or odd_or_even.lower() =="odd": 
        try: 
            place_wager = int(input("Please Enter Your Wager: ")) 
            if place_wager <= cash_total:
                print("You placed " + "$", place_wager, " Dollars on ", odd_or_even)
                print('\n')
                dice_1 = randint(1, 6)
                dice_2 = randint(1, 6)
                input("Press Enter to roll both dice ")
                print('\n')
                print("Dice 1 = ", dice_1)
                print("Dice 2 = ", dice_2)
                print('\n') 
                sum_of_two_dice = dice_1 + dice_2
                remainder = sum_of_two_dice % 2
            if remainder == 0 and odd_or_even.lower() == "even":
                cash_total = place_wager + cash_total
                print("The sum of the two dice is an Even Number!")
                print("You Won!!!")
                print("Total cash is $", cash_total)
            elif remainder == 1 and odd_or_even.lower() == "odd":
                cash_total = place_wager + cash_total
                print("The sum of the two dice is an Odd Number!")
                print("You Won!!!")
                print("Total cash is $", cash_total)

            else:
                cash_total = cash_total - place_wager
                print("Sorry, You Lost!!!")
                print("Total cash is $", cash_total)
                play = (input("Do you want to play again? Y/N \n"))
                if play.upper() == "Y":
                    cho_han()
                elif play.upper() == "N":
                    print("Thank you for playing!")
                elif cash_total==0:
                    print("You've run out of money, sorry!")
                else: 
                    print("You don't have enough money, try again!")
                    cho_han()
        except ValueError:
            print("The inputted value is not an integer, please try again.")
            cho_han()
    else:
        print("Invalid answer, please try again.")
        cho_han()
cho_han()