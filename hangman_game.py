import random

WORDS = ["python", "computer", "program", "keyboard", "internet"]

def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("=== HANGMAN GAME ===")
    print("Guess the word one letter at a time.")

    while wrong_guesses < max_wrong_guesses:
        display = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("\nWord:", display)
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            return

        guess = input("Enter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Sorry, that letter is not in the word.")

    print("\nYou ran out of guesses. The word was:", secret_word)

if __name__ == "__main__":
    play_hangman()
