import random
from hangman_words import word_list
from hangman_stages import stages, logo

chosen_word = random.choice(word_list)

# Testing code
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = ['_'] * len(chosen_word)
print(stages[6])
print(display)
player_lives = 6

while player_lives > 0:
    if "_" in display:
        guess = input("Guess a letter: ").lower()
        
        found = False
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                found = True
                if guess not in display:
                    print(f"'{guess}' is in the word. Keep going!")
                elif guess in display:
                    print(f"You have already guessed {guess}. Try a different letter.")
        if not found:
            player_lives -= 1
            print(f"'{guess}' isn't in the word. You lose a life ;-;")
        print(stages[player_lives])    
        print(display)
        print(f"Player Lives: {player_lives}")
    else:
        print("You Win!")
        break

if player_lives <= 0:
    print("You Lose.")
