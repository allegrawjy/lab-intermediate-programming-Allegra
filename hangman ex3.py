def updateText(water):
    guess = "_ " * len(water)
    correct = []
    wrong_guesses = 0 
    guessed_letters = []

    while True:
        print("Guess letter", guess)
        letter = input("Enter letter: ").lower()

        if letter in guessed_letters:
            print("Letter already guessed. Please try a different letter.")
            continue
        else:
            guessed_letters.append(letter)

        if letter in water:
            correct.append(letter)
            newguess = ""
            for i in range(0, len(water)*2, 2): 
                if water[i//2] == letter:
                    newguess += letter + " "
                else:
                    newguess += guess[i:i+2]  
            guess = newguess
            print("Congratulations! You have guessed the correct letter")
            if "_" not in guess:
                print("Congratulations! You have guessed the correct word!")
                break
        elif not letter.isalpha():
            print("Please input a letter")
        else:
            print("Incorrect, please guess again")
            wrong_guesses += 1
            print(f"Wrong guesses left: {6 - wrong_guesses}")
        
        if wrong_guesses == 6:
            print("You have run out of guesses. The word was:", water)
            break

updateText('smile')