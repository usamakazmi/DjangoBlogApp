# %pip install tweet-preprocessor
# %pip uninstall preprocessor
# %pip install emoji

# Set of libraries to import
import numpy as np
import pandas as pd
import preprocessor
import emoji

import re
import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('averaged_perceptron_tagger')
import spacy
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

pd.options.mode.chained_assignment = None

# Correcting Misspell words
misspell_data = pd.read_csv("theblog/aspell.txt",sep=":",names=["correction","misspell"])
misspell_data.misspell = misspell_data.misspell.str.strip()
misspell_data.misspell = misspell_data.misspell.str.split(" ")
misspell_data = misspell_data.explode("misspell").reset_index(drop=True)
misspell_data.drop_duplicates("misspell",inplace=True)
miss_corr = dict(zip(misspell_data.misspell, misspell_data.correction))

def misspelled_correction(text):
    for x in text.split(): 
        if x in miss_corr.keys(): 
            text = text.replace(x, miss_corr[x]) 
    return text

# Contractions
contractions = pd.read_csv("theblog/contractions.csv")
contractions.drop_duplicates(inplace=True)
cont_dic = dict(zip(contractions.Contraction, contractions.Meaning))

def cont_to_meaning(text): 
    for x in text.split(): 
        if x in cont_dic.keys(): 
            text = text.replace(x, cont_dic[x]) 
    return text

# Remove URL's and mentions
preprocessor.set_options(preprocessor.OPT.MENTION, preprocessor.OPT.URL)

# Lower Case
def lowerCase(df):
    return df["Content"].str.lower()

# Removing Punctuation
PUNCT_TO_REMOVE = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

# Removing Slang Words
slang_dict = dict()
with open('theblog/slang.txt') as f:
    data = f.readlines()
    for line in data:
        splitted = line.strip().split('=')
        slang_dict[splitted[0].lower()] = splitted[1].lower()
        
def modify_slang(text):
    splitted = text.split()
    modified = []
    for word in splitted:
        if word in slang_dict:
            modified.append(slang_dict[word])
        else:
            modified.append(word)
            
    return ' '.join(modified)

# Stopwords
def remove_stopwords(text):
    Stopwords = set(stopwords.words('english'))
    return " ".join([word for word in str(text).split() if word not in Stopwords])

# Stemming
def stem_words(text):
    stemmer = PorterStemmer()
    return " ".join([stemmer.stem(word) for word in text.split()])

# Lemmantization
def lemmatize_words(text):
    lemmatizer = WordNetLemmatizer()
    wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}

    pos_tagged_text = nltk.pos_tag(text.split())
    # print(pos_tagged_text)
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])

def proceprocessData(df):
    temp_df = df
    temp_df['Proprocessed_Content'] = temp_df['Content'].apply(lambda text: cleanData(text))
    temp_df.drop_duplicates(inplace=True)
    # temp_df.isna()
    temp_df.dropna()
    return temp_df

def cleanData(text):
    text = str(text).lower()     # Lower Case
    text = preprocessor.clean(text)    # Removing URL's and mentions
    text = ' '.join(remove_punctuation(emoji.demojize(text)).split())   # Remove punctuations and emoji's
    # text = remove_punctuation(text)
    text = misspelled_correction(text)  # Correcting misspelled Words
    text = cont_to_meaning(text)    # Remove contraction with meaning
    text = modify_slang(text)   # Removing slang words
    text = remove_stopwords(text) # Removing Stopwords

    return text