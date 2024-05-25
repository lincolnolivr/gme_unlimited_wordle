# %%
import os
import re
import chardet
import pandas as pd

# %%
source_path = 'data/raw'
english_words_path = os.path.join(os.getcwd(), '..', '..', source_path, 'english')
english_words_save_path = os.path.join(os.getcwd(), '..', '..', 'data/processed/english.csv')

# %%
dictonary = pd.DataFrame()
for file in os.listdir(english_words_path): 
    path = os.path.join(english_words_path, file)
    with open(path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']  
    
    df = pd.read_csv(path, on_bad_lines='skip', encoding=encoding ,engine='python', names=['Word'])
    dictonary = pd.concat([df, dictonary])
# %%
word_list = []

only_words = re.compile(r'^[a-zA-Z]+')

for word in dictonary.Word.unique():
    if re.match(only_words, str(word)):
       word_list.append(re.findall(only_words, str(word))[0])

word_list = list(set(word_list))
dictonary = pd.DataFrame(word_list, columns=['word'])
dictonary.to_csv(english_words_save_path, index=False)
# %%
