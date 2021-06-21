from preprocessing import * 
from model import *
# import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Filename = filename.csv

# importing data
print('Importing File')
df = pd.read_excel('theblog/Sadsong1.xls')
df = df.astype(str)
print('File Imported')

# Preprcoessing
print('\nPreprocessing Started')
df_2 = proceprocessData(df)
df_2['text_lemmatized'] = df_2['Content'].apply(lambda text: lemmatize_words(text))
print('Preprocessing End')

filter_df = df_2[['text_lemmatized']]
filter_df = filter_df.astype(str)
filter_df.drop_duplicates(keep='first', inplace=True)


# prediction
Prediction = prediction(filter_df)
filter_df['Sentiment'] = Prediction
filter_df.to_csv('label.csv', index=False)