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
images = [rock, paper, scissors]

#Write your code below this line 👇
import random
random_move = random.randint(0, 2)

user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if 0 <= user_move <= 2:
  print(images[user_move])
else:
  print("Invalid choice, dummy!")

if random_move == user_move:
  result = "Draw"
elif random_move == 0 and user_move == 1:
  result = "You win!"
elif random_move == 1 and user_move == 2:
  result = "You win!"
elif random_move == 2 and user_move == 0:
  result = "You win!"
else:
  result = "You lose!"

print("Computer chose:")
print(images[random_move])
print(result)
