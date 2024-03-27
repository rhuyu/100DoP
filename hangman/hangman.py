import random
from hangman_words import word_list
from hangman_stages import stages, logo

chosen_word = random.choice(word_list)

print(logo)

# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create a hangman ASCII art and display the length of the word
display = ['_'] * len(chosen_word)
print(stages[6])
print(display)

#Setting player lives for the amount of tries they get
player_lives = 6

# Keeps the game going while player has lives
while player_lives > 0:
    #if there are '_' in the display then we will continue with our guess
    if "_" in display:
        # Have the player guess a letter and automatically lowercase it for consistency
        guess = input("Guess a letter: ").lower()
        # Creating a variable and setting it to false to check if it is in the display
        found = False
        
        # Check to see if we already have guessed that letter, if so have player guess again
        if guess in display:
            print(f"You have already guessed {guess}. Try a different letter.")
        
        # Using a for loop to iterate through the length of the chosen word. If that guess matches the chosen word during that index that we set found = true    
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                found = True
        
        # Check for if a letter is in the display or not already to put out a keep going message.        
        if found and guess not in display:
            print(f"'{guess}' is in the word. Keep going!")
        
        # Losing a life if letter not found and printing a statement that says so            
        if not found:
            player_lives -= 1
            print(f"'{guess}' isn't in the word. You lose a life ;-;") 
        
        # Printing the current game stage    
        print(stages[player_lives])    
        print(display)
        print(f"Player Lives: {player_lives}")
    
    # When there are no more '_' in the display you win. 
    else:
        print("You Win!")
        break

# If player lives hit 0 you lose. 
if player_lives <= 0:
    print("You Lose.")
