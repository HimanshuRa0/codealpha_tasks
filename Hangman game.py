import random

# List of words to choose from
word_list = ['python', 'developer', 'hangman', 'challenge', 'programming', 'simplilearn', 'cloud']

# Choose a random word from the list
word = random.choice(word_list)
word_letters = set(word)
guessed_letters = set()
attempts = 6  # Number of incorrect guesses allowed

print("Welcome to Hangman!")
print("_ " * len(word))  # Display blanks

while attempts > 0 and word_letters:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left.")

    # Display current progress
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print(' '.join(display_word))

# Final result
if not word_letters:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Game over! The word was: {word}")
