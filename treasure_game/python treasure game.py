print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Would you like to go left or right? ")
if direction == "left" or direction == "Left":
    aqua = input("Would you like to swim or wait? ")
    if aqua == "wait" or aqua == "Wait":
        door = input("Theres 4 doors in front of you.  One is red, one is blue, one is yellow, and the last door is grey. ")
        if door == "red" or door == "Red":
            print("You fall through the floor into a lava pit.  Game Over")
        elif door == "blue" or door == "Blue":
            print("A Minotaur was waiting and killed you.  Game Over")
        elif door == "yellow" or door == "Yellow":
            print("Huzzah! You win!!! You open the chest to find an enormous amount of gold!")
        else:
            print("GAME OVER")

    else:
        print("You are killed by a alligator while crossing.  Game Over")
else:
    print("You've found a mimic, it eats you.  Game Over")
