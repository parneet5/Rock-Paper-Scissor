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
game_images = [rock,paper,scissors]

print("Welcome to Rock, Paper, Scissor Game")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n"))

if user_choice >=0 and user_choice <= 2:
    print(f"\nYou choose:{user_choice}")
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer choose:{computer_choice}")
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("It is a draw!. Play Again")
elif user_choice == 0 and computer_choice == 1:
    print("You loose, computer wins")
elif user_choice == 0 and computer_choice == 2:
    print("You win, computer looses")
elif user_choice == 1 and computer_choice == 0:
    print("You win, computer looses")
elif user_choice == 1 and computer_choice == 2:
    print("You loose, computer wins")
elif user_choice == 2 and computer_choice == 0:
    print("You loose, computer wins")
elif user_choice == 2 and computer_choice == 1:
    print("You win, computer looses")
else:
    print("You entered an invalid number, Please try again !!")

print("\n\n\n\n\n\nDeveloped by: Parneet Kaur")
