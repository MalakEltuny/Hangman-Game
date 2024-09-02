import random


words = ["python", "programming", "hangman", "challenge", "code"]
word_to_guess = random.choice(words)


guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6


def display_word():
    display = ""
    for guess in word_to_guess:
        if guess in guessed_letters:
            display += guess + " "

        else:
            display += "_ "
    print(display.strip())


while incorrect_guesses < max_incorrect_guesses:
    display_word()


    guess = input("Guess a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue


    if guess in guessed_letters:
        print("You've already guessed that letter.")
    elif guess in word_to_guess:
        guessed_letters.append(guess)
        print("Good guess!")
    else:
        incorrect_guesses += 1
        guessed_letters.append(guess)
        print("Incorrect guess.")


    if all(letter in guessed_letters for letter in word_to_guess):
        print(f"Congratulations! You've guessed the word: {word_to_guess}")
        break  # Exit the while loop if the word is guessed correctly
else:
    # This else is associated with the while loop
    print(f"Sorry, you've run out of guesses. The word was: {word_to_guess}")


if __name__ == "__main__":
    display_word()
