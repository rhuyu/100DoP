alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Creating a bunch of checks for UX and confirmation checks for the user to be sure and won't crash the program
direction_check = False
shift_check = False
user_confirm = False
coding_complete = False
# Giant while loop to keep iterating through the whole game again if needed
while coding_complete == False:
    while direction_check == False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == 'encode' or direction == 'decode':
            direction_check = True
        else:
            print(f"Looks like {direction} isn't a valid answer. Please try again.\n")

    while user_confirm == False:        
        text = input("Type your message:\n").lower()
        text_confirm = input(f"Your message is: '{text}'. Confirm text? Y/N ").lower()
        if text_confirm == 'y':
            user_confirm = True

    while shift_check == False:
        shift_input = input("Type the shift number:\n")
        if shift_input.isdigit():
            shift = int(shift_input)
            shift_check = True
        else:
            print(f"Sorry, '{shift_input}' isn't a valid number. Please try again.\n")


    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(text, shift):
        # Calling for these variables to be able to affect variables outside of this function
        global coding_complete
        global direction_check 
        global shift_check
        global user_confirm
        # Need an empty variable so that we can fill our text with the for loop
        encoded = ""
        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        for char in text:
            if char in alphabet: # For each characater in text and if it's in alphabet
            # Take the current index and add the shifted number
            # Added the modulo operator to have an error check for lower letters in the alphabet to 'loop' through the list again
                shifted_index = (alphabet.index(char) + shift) % len(alphabet)
                # Now use that new index number to find the shifted letter 
                encoded += alphabet[shifted_index] 
        print(f"The encoded text is {encoded}")
        coding_check_local = False
        while coding_check_local == False:
            coding_check = input("Do you wish to continue encoding/decoding? Y/N: ").lower()
            if coding_check == 'n':
                coding_check_local = True
                coding_complete = True
            elif coding_check == 'y':
                coding_check_local = True
                direction_check = False
                shift_check = False
                user_confirm = False
            else:
                coding_check = input("Do you wish to continue encoding/decoding? Y/N: ").lower()

    #TODO-3: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
    def decrypt(text, shift):
        global coding_complete
        global direction_check 
        global shift_check
        global user_confirm
        #TODO-4: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text. 
        decoded = ""
        for char in text:
            if char in alphabet:
                shifted_index = (alphabet.index(char) - shift)
                decoded += alphabet[shifted_index]
        print(f"Your decoded text is {decoded}")
        coding_check_local = False
        while coding_check_local == False:
            coding_check = input("Do you wish to continue encoding/decoding? Y/N: ").lower()
            if coding_check == 'n':
                coding_check_local = True
                coding_complete = True
            elif coding_check == 'y':
                coding_check_local = True
                direction_check = False
                shift_check = False
                user_confirm = False
            else:
                coding_check = input("Do you wish to continue encoding/decoding? Y/N: ").lower()

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
