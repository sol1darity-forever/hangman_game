import random
from collections import Counter

words = ['apple', 'lemon', 'pear', 'strawberry', 'berry', 'peach']
word = random.choice(words)

letter_guessed = ''
attempts = len(word) + 2
flag = 0
correct = 0
total = 0

for i in word:
    print('_', end=' ')

try:
    while attempts > 0 and flag == 0:
        print()
        print('Attempts:', attempts)
        attempts -= 1

        try:
            guess = str(input('Enter a letter to guess: \n'))
        except:
            print('Enter only a letter')
            continue

        if not guess.isalpha():
            print('Enter ONLY A LETTER!')
            continue
        elif guess in letter_guessed:
            print('You have yet entered this letter')
            continue
        elif len(guess) > 1:
            print('Enter only A SINGLE LETTER!!!')
            continue
        else:
            k = word.count(guess)
            for _ in range(k):
                letter_guessed += guess
            total += 1
        for char in word:
            if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
                print(char, end=' ')
            elif char in letter_guessed and (Counter(letter_guessed) == Counter(word)):
                flag = 1
                print('The word is {}'.format(word))
                print()
                print('Congratulations! You won!')
                print('Total attempts:', total)
                break
            else:
                print('_', end=' ')



        if attempts <= 0 and flag == 0:
            print()
            print('You lost! Try again!')
except KeyboardInterrupt:
    print()
    print('Bye!')