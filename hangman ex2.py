def main():
    secretWord = "water"
    guessed_letters = []
    chances = 6
    while chances > 0:
        guess = input ("Guess a letter: ")
        if len(guess)!= 1:
            print("Please enter only one letter")
        elif not guess.isalpha():
            print("Please enter a letter")
        elif guess.lower() in guessed_letters:
            print("Letter already guessed")
        else:
            guessed_letters.append(guess.lower())
            if guess.lower() in secretWord.lower():
                print("You have guessed a letter!")
            else:
                chances -=1
                print("Try again. There are {}chances left.".format(chances))