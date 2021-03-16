import random                                                                                       #229 lines, 10 endings, 3 cheat codes
print("----------WELCOME TO ROCK PAPER SCISSORS GAME----------")                                    #code 1: loseallmoney - makes you lose all money on your next turn, regardless, so you can get a loan and access endings quicker
print("To start the game, you have 10 coins. \nEach time you play, you can bet up to 1000 coins.")  #code 2: seeallendings - when you get to the point that you have less money than how much you owe, and say no to playing again
print("If you win, you double the amount you bet. \nIf you lose, you lose everything you bet!\n")   #                        you will see all 7 endings for that decision
coins = 10                                                                                          #code 3: alwaysrock - every time the computer will choose rock, so choose paper to always win or scissors to always lose
dueSum = 0                                                                                          #To use the codes, enter it instead of betting and then enter a number
code1 = False
code2 = False
code3 = False
notEnded = True
maxNum = 4
while notEnded == True:
    if code1 == True:
        coins = 0
        code1 = False
    print("You have " + str(coins) + " coins.")
    if dueSum > 0:
        print("You still owe " + str(int(dueSum)) + " coins!")
    if coins == 0:
        print("\nYou are out of coins!")
        print("However, the game isn't over yet!")
        print("\nWith CBW Loans, you can borrow up to 1000 coins, \nwith the SMALL interest rate of 50%!")
        loanAmount = input("Surely you don't want the fun to end just yet, so what do you say? (y/n)\n")
        if loanAmount == "y":
            print("I'm so glad!")
            while True:
                wrongLoan = False
                try:    
                    loan = int(input("How much would you like to borrow? "))
                except:
                    print("\nSorry, sir, we do not loan NON INTEGERS (god what kind of idiot are you..?)\n")
                    wrongLoan = True
                if wrongLoan == False:
                    if loan >= 1 and loan <= 1000:
                        print("Perfect! We'll get that sorted for you right away!")
                        break
                    else:
                        print("An integer between 1 and 1000, please!\n")
            coins = loan
            dueSum = dueSum + (loan * 1.5)
            dueSum = round(dueSum)
            print("You have " + str(coins) + " coins.")
                        
        else:
            print("Okay, fine.")
            print("You're now banned from the casino, SO LEAVE!!!")
            break
    while True:
        if coins != 0:
            betAgain = False
            try:
                bet = input("How many coins would you like to bet on this round? ")
                if bet == "loseallmoney":
                    code1 = True
                elif bet == "seeallendings":
                    code2 = True
                elif bet == "alwaysrock":
                    code3 = True
                    maxNum = 1
                bet = int(bet)
            except:
                print("Enter an integer!")
                betAgain = True
            if betAgain == False:
                if bet > coins:
                    print("You must enter a bet that you can afford!")
                elif bet >= 1 and bet <= 1000:
                    break
                else:
                    print("You must enter a number between 1 and 1000!")
            
    playAgain = False
    while True:
        playerChoice = input("r/p/s\n")
        if playerChoice == "r" or playerChoice == "p" or playerChoice == "s":
            break
        else:
            print("Please enter either 'r', 'p' or 's'!\n")
    randomChoice = random.randint(1,maxNum)
    if randomChoice == 1:
        print("I choose rock!\n")
        if playerChoice == "p":
            print("You win! Well done!")
            coins = coins + bet
        elif playerChoice == "s":
            print("You lose! Haha!")
            coins = coins - bet
        else:
            print("We picked the same! Oh well!")

    elif randomChoice == 2:
        print("I choose paper!\n")
        if playerChoice == "s":
            print("You win! Well done!")
            coins = coins + bet
        elif playerChoice == "r":
            print("You lose! Haha!")
            coins = coins - bet
        else:
            print("We picked the same! Oh well!")

    else:
        print("I choose scissors!\n")
        if playerChoice == "r":
            print("You win! Well done!")
            coins = coins + bet
        elif playerChoice == "p":
            print("You lose! Haha!")
            coins = coins - bet
        else:
            print("We picked the same! Oh well!")

    if playAgain != True:
        reply = input("Would you like to play again?\n")
        if reply.startswith("Y") or reply.startswith("y"):
            print("Great!")
            print("\nReloading...\n")
        else:
            if dueSum > coins:
                print("Are you sure? \nYou still owe " + str(int(dueSum)) + " coins to the bank,")
                reply = input("And have only " + str(coins) + " coins left.\n" )
                if reply.startswith("Y") or reply.startswith("y"):
                    print("\n\n\nYou decide to flee, without paying back to the bank.\n")
                    notEnded = False
                    randomEnding = 0
                    if code2 == False:
                        randomEnding = random.randint(1,8)
                    else: 
                        randomEnding = 1
                    while True:
                        if randomEnding == 1:
                            print("After a few weeks of evading the cops,")
                            print("you somehow get across the border to Mexico,")
                            print("and continue to live there happily for years to come, \nwith your stolen money and an old goat.")
                            if code2 == False:
                                break
                            else:
                                randomEnding = randomEnding + 1
                                print("\n\n")
                        elif randomEnding == 2:
                            print("You try to flee, but are caught within hours of leaving.")
                            print("You are sentenced to 5 years in prison, but after 2 years,")
                            print("you attempt an escape with a few other inmates.")
                            print("You all get out of the walls, but you are old and slow,")
                            print("and while running into the woods are gunned down \nby the guards, dying instantly.")
                            if code2 == False:
                                break
                            else:
                                randomEnding = randomEnding + 1
                                print("\n\n")
                        elif randomEnding == 3:
                            print("You try to flee, but on your way out of the casino \nencounter a guard, who stands in your path.")
                            print("Not knowing what else to do, you grab the guards gun \nand precede to shoot him with it.")
                            print("After this, you feel a weird bubbly feeling inside of you.")
                            print("You've killed a man, and it felt so good.")
                            print("With this newfound taste for blood, \nyou go on to murder 97 other people in the casino")
                            print("in what is now known as the massacre of the century.")
                            print("You are caught and live on for 48 more years,")
                            print("in a mental asylum, alone.")
                            if code2 == False:
                                break
                            else:
                                randomEnding = randomEnding + 1
                                print("\n\n")
                        elif randomEnding == 4:
                            print("You try to flee, but on your way out of the casino \nencounter a guard, who stands in your path.")
                            print("Not knowing what else to do, you grab the guards gun \nand precede to shoot him with it.")
                            print("What have you done? You killed an innocent man.")
                            print("What if he had a family? Children?")
                            print("You cannot bare the pain, \nand blow your brains out onto the nice white tiles.")
                            if code2 == False:
                                break
                            else:
                                randomEnding = randomEnding + 1
                                print("\n\n")
                        elif randomEnding == 5:
                            print("When fleeing the casino, time seems to slow down.")
                            print("Holy light shines down upon from the heavens, \nand you feel a new power within you.")
                            print("After escaping the authorities, you spend a few months \nmastering these powers. You are a god.")
                            print("6 months after you fled the casino and gained these powers,")
                            print("you come back out into the world. But you want to be bad.")
                            print("Nobody can stop you as you ruthlessly murder everyone on earth.")
                            print("You are all that remains.")
                            print("And now, with your power, you can recreate the world.")
                            if code2 == False:
                                break
                            else:
                                randomEnding = randomEnding + 1
                                print("\n\n")
                        elif randomEnding == 6:
                            print("When fleeing the casino, time seems to slow down.")
                            print("Holy light shines down upon from the heavens, \nand you feel a new power within you.")
                            print("After escaping the authorities, you spend a few months \nmastering these powers. You are a god.")
                            print("6 months after you fled the casino and gained these powers,")
                            print("you come back out into the world. And now, you want to be good.")
                            print("You fly around the globe, helping all.")
                            print("The people now look up to you.")
                            print("You are their god, and this is your planet.")
                            if code2 == False:
                                break
                            else:
                                randomEnding = randomEnding + 1
                                print("\n\n")
                        else:
                            print("You flee the casino, and go to a remote farmhouse in Bridgeport.")
                            print("You steal the identity of former friend Pete, and live there for 3 years,")
                            print("until the truth is revealed and you are sent to prison.")
                            print("However, once you are released from prison, a series of bad events")
                            print("leads to you getting killed by a professional hitman in New York.")
                            break
                
            elif dueSum == 0:
                if coins < 10:
                    remainder = 10 - coins
                    print("You leave the casino in shame, having lost " + str(remainder) + " coins.")
                else:
                    remainder = coins - 10
                    print("You leave the casino happily, having gained " + str(remainder) + " coins!")
                break
            else:
                coins = coins - dueSum
                if coins < 10:
                    print("You pay back what you owe to the bank, \nyet leave the casino in shame with only " + str(coins) + " coins left.")
                else:
                    print("You pay back what you owe to the bank, \nand leave the casino happy, with " + str(coins) + " coins!")
                break

input("\n\nPress ENTER to exit")
