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
import random

print("Welcome to Rock , paper , scissors game,\n RULES:\n Type 0 for rock, 1 for paper and 2 for scissors  ")

user_choice=int(input("Enter your choice:"))
computer_choice= random.randint(0,2)

if user_choice==0 and computer_choice==2:
  print("you win!")

elif user_choice==0 and computer_choice==1:
  print("You lose:(")

elif user_choice==0 and computer_choice==0:
  print("It's a draw")

elif user_choice==1 and computer_choice==0:
  print("You win!")

elif user_choice==1 and computer_choice==1:
  print("Its a draw")

elif user_choice==1 and computer_choice==2:
  print("You lose ):")

elif user_choice==2 and computer_choice==0:
  print("You lose ):")

elif user_choice==2 and computer_choice==1:
  print("You win!")


elif user_choice==2 and computer_choice==2:
  print("Its a draw")

else:
  print("Your entry is invalid")



