import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock, paper, scissors]
choice = input("Please choose 0 for Rock, 1 for Paper, 2 for Scissors ")
computer_choice = random.choice(rock_paper_scissors)
if choice == "0":
    print("Rock\n")
    print(rock)
    if computer_choice == paper:
        print(paper)
        print("You lose.")
    elif computer_choice == scissors:
        print(scissors)
        print("You win!")
elif choice == "1":
    print("Paper\n")
    print(paper)
    if computer_choice == rock:
        print(rock)
        print("You win!")
    elif computer_choice == scissors:
        print(scissors)
        print("You lose.")
elif choice == "2":
    print("Scissors\n")
    print(scissors)
    if computer_choice == paper:
        print(paper)
        print("You win!")
    elif computer_choice == rock:
        print(rock)
        print("You lose.")
elif computer_choice == choice:
    print(computer_choice)
    print("Tie!")
else:
    print("Please enter a valid input!\n")
