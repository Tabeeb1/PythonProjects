import random
import hangman_words
import hangman_art

print(hangman_art.logo)
llist = hangman_words.word_list
art = hangman_art.stages
word = random.choice(llist)
len_of_word = len(word)
blank = []
i = 0
while i<len_of_word:
    blank.append("_")
    i += 1

total = 0
life = 6
while total < len_of_word and life > 0:
    letter = input("Guess a letter: ")
    if letter in word:
        j = 0
        for element in word:
            if element == letter:
                blank[j] = element
                j += 1
                total += 1
            else:
                j += 1
    else:
        life -= 1
        print(art[life])
    if life > 0:
        for item in blank:
            print(item,end = '')
    if life >0:
        print("\n")

if life == 0:
    print("You lose")
    print(f'The word was {word}')
else:
    print("You win")
