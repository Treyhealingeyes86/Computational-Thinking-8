print("You wake up with a throbbing headache and no memory of who or where you are.")
choice1 = input("You look around the damp, dark room you are in and notice a cabinet and window. Do you want to: open the   window or search the cabinet? ")
if choice1 == "open the window" or choice1 == "window":
    print("You ignore your headache and move to the window. You fail to pry it open and hurt your wrist.")
    choice2 = input("Do you want to search the cabinet? ")
    if choice2 == "yes" or choice2 == "Yes":
        print("You open the cabinet and find a notecard. A list of instructions is written on the other side, showing you how to escape.")
        choice3 = input("Follow the instructions? ")
        if choice3 == "yes" or choice3 == "Yes":
            print("You read the instructions and eventually find a hatch in the ceiling.")
            choice4 = input("After climbing out, you find yourself at a crossroads. With three options, do you go forward, left or      right? ")
            if choice4 == "forward" or choice4 == "Forward":
                print("You walk for days, wondering if you chose the right path. Right before your last sliver of hope withers    away, you find a grave.")
                print("You drag your eyes up the stone, noticing words like wonderful sibling and amazing friend along with tons  of flowers and messages.")
                name = input("At the very top, etched into weathered stone is the name: ")
                print(f"upon seeing the letters {name}, you fall to your knees, all your previous memories flooding back into your mind.")
                print(f"Truly, here lies {name}.")
            elif choice4 == "left" or choice4 == "Left":
                print("You follow the trail left down a misty road. Your surroundings turn darker as you go, and you have to dodge many traps.")
                print("At the end of the path lies a big gate, and an old traveler dressed in yellow robes greets you. As soon as you stare into his face, you fall to the ground.")
                print("Your journey ends here.")
            elif choice4 == "right" or choice4 == "Right":
                print("You wander the worn ground for days, days turn into weeks and months and you fall before you ever find an  answer.")
            else:
                print("Left, right or forward.")
        elif choice3 == "no" or choice3 == "No":
            print("Skeptical, you stay in that cold dark room forever.")
        else:
            print("Yes or no.")
    elif choice2 == "no" or choice2 == "No":
        print("After hours of sitting, you find a hatch in the ceiling and climb out. You managed to escape, but never    truly found who you were.")
    else:
        print("Yes or no.")
elif choice1 == "search the cabinet" or choice1 == "cabinet":
    print("You search through the cabinet and find a notecard.")
    choice5 = input("When you flip it over, you find a list of instructions telling you how to escape. Will you follow them? ")
    if choice5 == "Yes" or choice5 == "yes":
        print("You read the instructions and eventually find a hatch in the ceiling.")
        choice6 = input("After climbing out, you find yourself at a crossroads. With three options, do you go forward, left or      right? ")
        if choice6 == "forward" or choice6 == "Forward":
             print("You walk for days, wondering if you chose the right path. Right before your last sliver of hope withers    away, you find a grave.")
             print("You drag your eyes up the stone, noticing words like wonderful sibling and amazing friend along with tons  of flowers and messages.")
             name = input("At the very top, etched into weathered stone is the name: ")
             print(f"upon seeing the letters {name}, you fall to your knees, all your previous memories flooding back into your mind.")
             print(f"Truly, here lies {name}.")
        elif choice6 == "left" or choice6 == "Left":
            print("You follow the trail left down a misty road. Your surroundings turn darker as you go, and you have to dodge many traps.")
            print("At the end of the path lies a big gate, and an old traveler dressed in yellow robes greets you. As soon as you stare into his face, you fall to the ground.")
            print("Your journey ends here.")
        elif choice6 == "Right" or choice6 == "right":
            print("You wander the worn ground for days, days turn into weeks and months and you fall before you ever find an  answer.")
        else:
            print("Forward, left or right.")
    elif choice5 == "No" or choice5 == "no":
        print("Skeptical, you stay in that cold dark room forever.")
    else:
        print("Yes or no.")
elif choice1 == "eat breakfast" or choice1 == "eat":
    print("You can't eat! There's no food!")
else:
    print("You only have 2 options. Use lowercase.")