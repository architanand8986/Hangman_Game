import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(f"Pssst, the solution is {chosen_word}.")
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You have already guessed {guess}.Try guessing another alphabet.')
    i = 0
    for n in range(word_length):
        if guess == chosen_word[n]:
            print(f'You guessed {guess}.')
            display[n] = guess
            break
        else:
            i += 1
        if i == word_length:
            lives -= 1
            print(f"You have guess {guess} which is not in the word, so you lose a life.")
            print(stages[lives])

    print(f"{' '.join(display)}")

    if lives == 0:
        print("You lost")
        break
    if "_" not in display:
        end_of_game = True
        print("You win.")

