import random

words = ['apple', 'grape', 'mango', 'peach', 'lemon']
word = random.choice(words)
guessed = []
tries = 6

while tries > 0:
    display = ''
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += '_'

    print('Word:', ' '.join(display))

    if '_' not in display:
        print('You won! The word was:', word)
        break

    guess = input('Guess a letter: ').lower()

    if guess in guessed:
        print('Already guessed.\n')
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print('Wrong! Tries left:', tries, '\n')

if tries == 0:
    print('You lost! The word was:', word)