print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Dragon Ball Quest.")
print("Your mission is to find all 7 Dragon Balls and summon Shenron!\n")

first_question = input("Fly to West City or head to the forest? ").strip().lower()

if first_question == "west city":
    print("Fall into a trap set by the Red Ribbon Army. Game Over.")
elif first_question == "forest":
    print("You carefully make your way through the forest...\n")
    second_question = input("Cross the river or wait for Nimbus? ").strip().lower()

    if second_question == "cross the river":
        print("You try to cross... but are attacked by a wild Saibaman! Game Over.")
    elif second_question == "wait for nimbus":
        print("Nimbus arrives just in time! You soar above the river.\n")
        third_question = input("Choose a portal: Red, Blue, or Yellow? ").strip().lower()

        if third_question == "red":
            print("You enter a burning lava dimension — Burned by fire. Game Over.")
        elif third_question == "blue":
            print("You fall into the Dark World — Eaten by beasts. Game Over.")
        elif third_question == "yellow":
            print("You enter the Sacred Temple and find the final Dragon Ball.\n✨ You Win! Shenron is summoned! ✨")
        else:
            print("You wander into the Hyperbolic Time Chamber and get lost. Game Over.")
    else:
        print("Confused, you hesitate... and get ambushed. Game Over.")
else:
    print("You fly off in the wrong direction and get caught by Frieza's scouts. Game Over.")
