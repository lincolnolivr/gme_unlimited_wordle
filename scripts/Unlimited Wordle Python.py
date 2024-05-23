# %%
__version__ = '1.0.0'

# %%
import os
import time
import random
import chardet
import easygui
import pandas as pd
from icecream import ic
from colorama import Fore, Back, Style

# %%
chances = 3
word_size = [4, 5, 6, 7, 8]
dictonary_path = 'data/raw'
english_path = os.path.join(os.getcwd(), '..', dictonary_path, 'english')

# %%
dictonary = pd.DataFrame()

print('Carregando palavras...')
for file in os.listdir(english_path): 
    path = os.path.join(english_path, file)
    with open(path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']  
    
    df = pd.read_csv(path, on_bad_lines='skip', encoding=encoding ,engine='python', names=['Word'])
    dictonary = pd.concat([df, dictonary])

# %%
word_list = [str(word).strip() for word in dictonary.Word.unique()]
size_choice = int(easygui.choicebox('Escolha a quantidade de letras para jogar', 'Escolha o modo de jogo', word_size))
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

    for letter in input_word:
        if letter not in alphabet:
            print('Caractere inválido, tente de novo')
            break
    else:
        pass

    if input_word in used_words:
        print(f'\nPalavra já utilizada, insira outra palavra.')
        continue

    if input_word not in word_list_filtered:
        print(f'\nPalavra não válida, tente de novo')
        continue
    
    elif len(input_word) != size_choice:
        print('\nTamanho de palavra incorreto, tente de novo')
        continue
        
    elif input_word == selected_word:
        print(f'\nParabéns, você ganhou!! A palavra é: {selected_word}')
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
            os.system('pause')
        break

    elif current_chances == 1:
        print(f'\nPoxa, você perdeu. A palavra correta era: {selected_word}')
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
            os.system('pause')
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
        print(f'Palavras Já Utilizadas: {used_words}')
        print(f'Letras já utilizadas palavra: {used_letters}')
        print(f'Letras na palavra: {letters_in_word}')
        print()

        for i in range(size_choice):
            if input_word[i] == selected_word[i]:
                answer = ''.join(answer[:i]) + input_word[i] + ''.join(answer[i+1:])
            if input_word[i] in selected_word:
                print(f'A letra {input_word[i]} está na palavra')
            if input_word[i] not in selected_word:
                print(f'A letra {input_word[i]} não está na palavra')
            
        print('\n' + ' '.join(answer))



