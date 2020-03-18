#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:35:05 2020

@author: malcolmmccabe
"""

"""
Recurrent Neural Networks for Language Modeling - Ch. 1
"""

'''
Introduction to Language Models
'''

#GETTING USED TO TEXT DATA

sheldon_quotes = ["You're afraid of insects and women, Ladybugs must render \
                  you catatonic.", 'Scissors cuts paper, paper covers rock, \
                  rock crushes lizard, lizard poisons Spock, Spock smashes \
                  scissors, scissors decapitates lizard, lizard eats paper, \
                  paper disproves Spock, Spock vaporizes rock, and as it \
                  always has, rock crushes scissors.']

#Transform list of sentences into list of words
all_words = ' '.join(sheldon_quotes).split(' ')

#Get number of unique words
unique_words = list(set(all_words))

#Dictionary of indexes as keys and words as values
index_to_word = {i:wd for (i,wd) in enumerate(sorted(unique_words))}

print(index_to_word)

#Dictionary of words as keys and indexes as values
word_to_index = {wd:i for (i,wd) in enumerate(sorted(unique_words))}

print(word_to_index)

#PREPARING TEXT DATA FOR MODEL INPUT 

#Create lists to keep sentences and next character
sentences = []      # ~ Training data
next_chars = []     # ~ Training labels

#Define hyperparameters
step = 2            # ~ 2 Steps to take when reading texts in characters
chars_window = 10   # ~ 10 characters to use to predict next one

#Loop over text: length 'chars_window' per time with step equal to 'step'
for i in range(0, len(sheldon_quotes) - chars_window, step):
    sentences.append(sheldon_quotes[i:i + chars_window])
    next_chars.append(sheldon_quotes[i + chars_window])
    
#Print 10 pairs
print_examples(setences, next_chars, 10)

#TRANSFORMING NEW TEXT
new_text = ['A man either lives life as it happens to him meets it head-on \
            and licks it or he turns his back on it and starts to wither \
            away', 'To the brave crew and passengers of the Kobayshi Maru \
            sucks to be you', 'Beware of more powerful weapons They often \
            inflict as much damage to your soul as they do to you enemies', 
            'They are merely scars not mortal wounds and you must use them to \
            propel you forward', 'You cannot explain away a wantonly immoral \
            act because you think that it is connected to some higher purpose']

#Loop through the sentences and get indexes 
new_text_split = []
for sentence in  new_text:
    sent_split = []
    for wd in sentence.split(' '):
        index = word_to_index.get(wd, 0)
        sent_split.append(index)
    new_text_split.append(sent_split)
    
#Print first sentence's indexes
print(new_text_split[0])

#Print sentence converted using dictionary
print(' '.join([index_to_word[index] for index in new_text_split[0]]))

'''
Introduction to RNN inside Keras
'''

#KERAS MODELS

#Import required modules
from keras.models import Sequential
from keras.layers import LSTM, Dense

#Instantiate model class 
model = Sequential(name="sequential_model")

#Add LSTM layer (defining input shape b/c initial layer)
model.add(LSTM(128, input_shape=(None, 10), name="LSTM"))
model.add(Dense(1, activation="sigmoid", name="output"))

model.summary()

#Define input layer
main_input = Input(shape=(None, 10), name="input")

#One LSTM layer (input shape is already defined)
lstm_layer = LSTM(128, name="LSTM")(main_input)

#Add dense layer with one unit
main_output = Dense(1, activation="sigmoid", name="output")(lstm_layer)

#Instantiate class at the end
model = Model(inputs=main_input, outputs=main_output, name="modelclass_model")

#Same amount of parameters to train as before
model.summary()

#KERAS PREPROCESSING

texts = ['So if a photon is directed through a plane with two slits in it and \
         either slit is observed it will not go through both slits. If it’s \
         unobserved it will, however, if it’s observed after it’s left the \
         plane but before it hits its target, it will not have gone through \
         both slits. Hello, female children. Allow me to inspire you with a \
         story about a great female scientist. Polish-born, French-educated \
         Madame Curie. Co-discoverer of radioactivity, she was a hero of \
         science, until her hair fell out, her vomit and stool became filled \
         with blood, and she was poisoned to death by her own discovery. With \
         a little hard work, I see no reason why that can’t happen to any of \
         you. Are we done? Can we go?']


#Import relevant classes/functions
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

#Build dictionary of indexes
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

#Change texts into sequence of indexes
texts_numeric = tokenizer.texts_to_sequences(texts)
print("Number of words in the sample texts: ({0}, {1})".format(len(texts_numeric[0]), len(texts_numeric[1])))

#Pad the sequences
texts_pad = pad_sequences(texts_numeric, 60)
print("Now the texts have fixed length: 60. Let's see the first one: \n{0}".format(texts_pad[0]))

#YOUR FIRST RNN MODEL

#Build Model
model = Sequential()
model.add(SimpleRNN(units=128, input_shape=(None, 1)))
model.add(Dense(unit=1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Load pre-trained weights
model.load_weights('model_weights.h5')

#Method '.evaluate()' shows the loss and accuracy
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print("Loss: {0} \nAccuracy: {1}".format(loss,acc))










