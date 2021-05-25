from sklearn.model_selection  import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import RepeatedKFold, cross_val_score
from sklearn import metrics
import joblib
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

def prediction(filter_df):
    # Train Test Split
    # X_train, X_test, Y_train, Y_test = train_test_split(list(filter_df['text_lemmatized']), list(filter_df['Sentiment']), test_size=0.25, random_state=42)
    X_test = filter_df['text_lemmatized']

    # Loading tfidf pickle file
    tf_filename = 'theblog/fidf1.sav'
    tf = joblib.load(open('theblog/tfidf1.sav', 'rb'))

    tfidf_new = TfidfVectorizer(stop_words='english', max_df=0.25, ngram_range=(1,3), vocabulary= tf.vocabulary_)
    X_test_final = tfidf_new.fit_transform(X_test)

    # Load the model
    print('\nModel Loading...')
    filename = 'theblog/finalized_model.sav'
    loaded_model = joblib.load(open(filename, 'rb'))
    print('Model Loaded.')

    # Prediction
    print('\nPredicting Sentiment...')
    final_prediction = loaded_model.predict(X_test_final)
    print('Prediction Completed.')

    return final_prediction