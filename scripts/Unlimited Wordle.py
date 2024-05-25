# %%
__version__ = '2.1.2'

# %%
import os
import csv
import re
import random
import chardet
import pandas as pd
from colorama import Fore, Back, Style

# %%
def find_all(substring: str, list: list[str]):
    return [letter.start() for letter in re.finditer(substring, list)]

def almost_letter(letter):
    print(f'{Back.YELLOW}{Fore.BLACK}{letter}', end=f'')
    print(f'{Style.RESET_ALL}', end=' ')

def wrong_letter(letter):
    print(f'{letter}', end=f'')
    print(f'{Style.RESET_ALL}', end=' ')

def correct_letter(letter):
    print(f'{Back.GREEN}{letter}', end=f'')
    print(f'{Style.RESET_ALL}', end=' ')

# %%
chances = 6
word_size = [4, 5, 6, 7, 8]
dictonary_path = os.path.join(os.getcwd(), '..', 'data/processed/english.csv')
with open(dictonary_path) as dictonary:
    reader = csv.reader(dictonary, delimiter=',', quotechar='\'')
    word_list = [row[0] for row in reader]
    
size_choice = int(input(f'Escolha a quantidade de letras para jogar (digite um número de {min(word_size)} a {max(word_size)}): '))

while size_choice not in word_size:
    print(f'\nTamanho inválido, por favor escolha um número entre {min(word_size)} e {max(word_size)}')
    size_choice = int(input(f'\nEscolha a quantidade de letras para jogar (digite um número de {min(word_size)} a {max(word_size)}): '))
     
if size_choice >= 5:
    chances += int(size_choice - 5)

word_list_filtered = [word.upper() for word in word_list if len(word)==int(size_choice)]
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z']

# %%
selected_word = random.choice(word_list_filtered)
used_words = []
used_letters = []
letters_in_word = []
answer = [space for space in '_' * size_choice]
current_chances = chances

print(f'\nChances Restantes: {current_chances}')
print(' '.join(answer))

while True:
    # Verificar possibilidade de limitar caracteres de acordo com o tamanho escolhido
    print()
    input_word = str(input('Escolha uma palavra: ')).upper()

    invalid_caracter = [letter for letter in input_word if letter not in alphabet]

    if len(invalid_caracter) > 0:
        print('Caractere inválido, tente de novo')
        continue

    if input_word in used_words:
        print(f'\nPalavra já utilizada, insira outra palavra.')
        continue

    elif len(input_word) != size_choice:
        print('\nTamanho de palavra incorreto, tente de novo')
        continue

    elif input_word not in word_list_filtered:
        print(f'\nPalavra não válida, tente de novo')
        continue
        
    elif input_word == selected_word:
        print(f'\nParabéns, você ganhou!! A palavra é: {selected_word}')
        continue_game = input('\nDeseja continuar? Digite (Y/N)...')

        while continue_game.upper() != 'Y' and continue_game.upper() != 'N':
            print('\nOpção inválida, tente de novo')
            continue_game = input('\nDeseja continuar? Digite (Y/N)...')

        if continue_game.upper() == 'Y':
            selected_word = random.choice(word_list_filtered)
            used_words = []
            used_letters = []
            letters_in_word = []
            answer = [space for space in '_' * size_choice]
            current_chances = chances
            print(f'\nChances Restantes: {current_chances}')
            print(' '.join(answer))
            continue
        else:
            print('\nObrigado por jogar, até a próxima!')
        break

    elif current_chances == 1:
        print(f'\nPoxa, você perdeu. A palavra correta era: {selected_word}')
        continue_game = input('\nDeseja continuar? Digite (Y/N)...')

        while continue_game.upper() != 'Y' and continue_game.upper() != 'N':
            print('\nOpção inválida, tente de novo')
            continue_game = input('\nDeseja continuar? Digite (Y/N)...')

        if continue_game.upper() == 'Y':
            selected_word = random.choice(word_list_filtered)
            used_words = []
            used_letters = []
            letters_in_word = []
            answer = [space for space in '_' * size_choice]
            current_chances = chances
            print(f'\nChances Restantes: {current_chances}')
            print(' '.join(answer))
            continue
        else:
            print('\nObrigado por jogar, até a próxima!')
        break
    
    else:
        current_chances -= 1
        used_words.append(input_word)

        for letter in input_word:
            used_letters.append(letter)
            used_letters = list(set(used_letters))
            used_letters.sort()
            if letter in selected_word:
                letters_in_word.append(letter)
                letters_in_word = list(set(letters_in_word))
                letters_in_word.sort()

        print(f'\nChances Restantes: {current_chances}')
        print(f'Letras já utilizadas palavra: {used_letters}')
        print()

        for index, letter in enumerate(input_word):
            if input_word[index] == selected_word[index]:
                correct_letter(letter)

            elif input_word[index] in selected_word:
                guess_occurences = find_all(input_word[index], input_word)
                word_occurences = find_all(input_word[index], selected_word)
                quantity_in_input_word = input_word.count(input_word[index])
                quantity_in_selected_word = selected_word.count(input_word[index])
                corrects = [i for i in word_occurences if i in guess_occurences]
                wrongs = [i for i in guess_occurences if i not in word_occurences]

                if quantity_in_selected_word >= quantity_in_input_word:
                    almost_letter(letter)
                elif quantity_in_input_word ==1:
                    almost_letter(letter)
                elif index == guess_occurences[0] and (quantity_in_selected_word !=1 or len(corrects)==0):
                    almost_letter(letter)
                elif index in wrongs[:(len(wrongs) - len(corrects))] and quantity_in_input_word < quantity_in_selected_word:
                    almost_letter(letter)
                else:
                    wrong_letter(letter)

            elif letter not in selected_word:
                wrong_letter(letter)
            
        print('\n' + ' '.join(answer))


