import random

# Defining variables 
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
              
# Asking for player input and printing out their answer


# Prompt the player for their choice
player = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

# Check if the input is not valid (not one of 0, 1, or 2)
while player not in ['0', '1', '2']:
    print("Invalid input. Please type a valid answer!")
    player = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
    
player = int(player)

if player == 0:
    print(f'Player Choice:\n{rock}')
elif player == 1:
    print(f'Player Choice:\n{paper}')
elif player == 2:
    print(f'Player Choice:\n{scissors}')
    
# Have computer choose random value
computer = random.randint(0,2)
if computer == 0:
    print(f'Computer Choice:\n{rock}')
elif computer == 1:
    print(f'Computer Choice:\n{paper}')
elif computer == 2:
    print(f'Computer Choice:\n{scissors}')
    
    
# Annoucing the result (0 = rock, 1 = paper, 2 = scissors)
if player == computer:
    print ("Awhhh it's a draw! Better luck next time!")
elif player == 0:
    if computer == 1:
        print("Uh oh, computer chose paper! You lose ;-;")
    else:
        print("HAHA! YOU WIN!")     
elif player == 1:
    if computer == 2:
        print("Uh oh, computer chose scissors! You lose ;-;")
    else:
        print("HAHA! YOU WIN!")
elif player == 2:
    if computer == 0:
        print("Uh oh, computer chose rock! You lose ;-;")
    else:
        print("HAHA! YOU WIN!")
    
