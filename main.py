from words import words
import random
import string
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    lives = 6
    word = get_valid_word(words)
    alphabet = set(string.ascii_uppercase)
    letters_word = set(word)
    used_letters = set() 

  
    while len(letters_word) > 0 and lives > 0:
        print('Tienes', lives, 'vidas y has intentado con estas letras: ', ' '.join(used_letters))
       
       
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palabra a adivinar: ', ' '.join(word_list))

        user_letter = input('Adivina la letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_word:
                letters_word.remove(user_letter)
                print('')

            else:
                lives = lives - 1 
                print('\nLa letra,', user_letter, 'no esta en la palabra.')

        elif user_letter in used_letters:
            print('\nYa utilizaste esta letra, intenta con otra letra')

        else:
            print('\nNo es una letra valida')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('Perdiste, lo siento. La palabra era', word)
    else:
        print('Bien! Adivinaste la palabra', word,)


if __name__ == '__main__':
    hangman()

