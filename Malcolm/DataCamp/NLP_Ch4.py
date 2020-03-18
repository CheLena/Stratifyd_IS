#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:43:23 2020

@author: malcolmmccabe
"""

"""
NLP - Ch. 4 Notes 
"""

#Goal: Predict Movie Genre

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

#Reads in csv file as DataFrame
data = pd.read_csv("/Users/malcolmmccabe/Desktop/Python File/fake_or_real_news.csv")

#Prints head of data
#print(data.head())

#Create series to store label
y = data.label

#Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], y, 
        test_size=0.33, random_state=53)

#Initaialize CountVectorizer object
count_vectorizer = CountVectorizer(stop_words='english')

#Transform training data using only 'text' column values
count_train = count_vectorizer.fit_transform(X_train)

#Transform test data using only 'text' column values
count_test = count_vectorizer.transform(X_test)

#Print first 10 features of count_vecotrizer
#print(count_vectorizer.get_feature_names()[:10])

from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize a TfidfVectorizer object: tfidf_vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Transform the training data: tfidf_train 
tfidf_train = tfidf_vectorizer.fit_transform(X_train.values)

# Transform the test data: tfidf_test 
tfidf_test = tfidf_vectorizer.transform(X_test.values)

# Print the first 10 features
#print(tfidf_vectorizer.get_feature_names()[:10])

# Print the first 5 vectors of the tfidf training data
#print(tfidf_train.A[:5])

# Create the CountVectorizer DataFrame: count_df
count_df = pd.DataFrame(count_train.A, columns=count_vectorizer.get_feature_names())

# Create the TfidfVectorizer DataFrame: tfidf_df
tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vectorizer.get_feature_names())

# Print the head of count_df
#print(count_df.head())

# Print the head of tfidf_df
#print(tfidf_df.head())

# Calculate the difference in columns: difference
difference = set(count_df.columns) - set(tfidf_df.columns)
#print(difference)

# Check whether the DataFrames are equal
#print(count_df.equals(difference))
    
'''
Naive Bayes
* Determines accuracy of association 
'''

from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB

'''
Analyze CountVectorizer
'''

# Instantiate a Multinomial Naive Bayes classifier: nb_classifier
nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(count_train, y_train)

# Create the predicted tags: pred
pred = nb_classifier.predict(count_test)

# Calculate the accuracy score: score
score = metrics.confusion_matrix(y_test, pred, labels=['FAKE','REAL'])
#print(score)

# Calculate the confusion matrix: cm
cm = metrics.accuracy_score(y_test, pred)
#print(cm)

'''
Now analyze TfidfVectorizer
'''
# Create a Multinomial Naive Bayes classifier: nb_classifier
nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(tfidf_train, y_train)

# Create the predicted tags: pred
pred = nb_classifier.predict(tfidf_test)

# Calculate the accuracy score: score
score = metrics.accuracy_score(y_test, pred)
#print(score)

# Calculate the confusion matrix: cm
cm = metrics.confusion_matrix(y_test, pred, labels=['FAKE','REAL'])
#print(cm)

'''
Improving the model
'''

import numpy as np

# Create the list of alphas: alphas
alphas = np.arange(0,1,0.1)

# Define train_and_predict()
def train_and_predict(alpha):
    # Instantiate the classifier: nb_classifier
    nb_classifier = MultinomialNB(alpha=alpha)
    # Fit to the training data
    nb_classifier.fit(tfidf_train, y_train)
    # Predict the labels: pred
    pred = nb_classifier.predict(tfidf_test)
    # Compute accuracy: score
    score = metrics.accuracy_score(y_test, pred)
    return score

# Iterate over the alphas and print the corresponding score

#for alpha in alphas:
#    print('Alpha: ', alpha)
#    print('Score: ', train_and_predict(alpha))
#    print()

'''
Inspecting the model
'''
# Get the class labels: class_labels
class_labels = nb_classifier.classes_

# Extract the features: feature_names
feature_names = tfidf_vectorizer.get_feature_names()

# Zip the feature names together with the coefficient array and sort by weights: feat_with_weights
feat_with_weights = sorted(zip(nb_classifier.coef_[0], feature_names))

# Print the first class label and the top 20 feat_with_weights entries
print(class_labels[0], feat_with_weights[:20])

# Print the second class label and the bottom 20 feat_with_weights entries
print(class_labels[1], feat_with_weights[-20:])