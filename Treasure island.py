print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer = input('You are at a cross road where do you go from here? "left" or "right"? \n').lower() 
if answer == "left":
  answer2 = input('You come to a river. There is a beautiful city in the middle of the river. Type "wait" to wait for a ship. Type "swim" to swim across. \n').lower()
  if answer2 == "wait":
    answer3 = input('You get to the Island and you see three doors. Type "red" for door one. Type "blue" for door two. Type "yellow" for door three. \n').lower()
    if answer3 == "yellow":
      print("Treasure found.You Win!")
    elif answer3 == "red":
      print("Stung by bees. Game Over.")
    elif answer3 == "blue":
      print("room was boobie trapped. Game Over.")
    else:
      print("Game Over!")
  else:
    print("You got swallowed by a shark.Game over.")
else:
 print("You were attacked by savages.Game Over.")
