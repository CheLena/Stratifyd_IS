#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:28:31 2020

@author: malcolmmccabe
"""

"""
Recurrent Neural Networks for Language Modeling - Ch. 2
"""

'''
Vanishing and exploding gradients
'''

#EXPLODING GRADIENT PROBLEM 

#Create Keras model with one hidden Dense layer
model = Sequential()
model.add(Dense(25, input_dim=20, activation='relu', kernel_initializer=he_uniform(seed=42)))
model.add(Dense(1, activation='linear'))

#Compile and fit the model
model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.01, momentum=0.9, clipvalue=3.0))
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, verbose=0)

#See Mean Square Error for train and test data
train_mse = model.evaluate(X_train, y_train, verbose=0)
test_mse = model.evaluate(X_test, y_test, verbose=0)

#Print values of MSE
print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))

#VANISHING GRADIENT PROBLEM

#Create Keras Model 
model = Sequential()
model.add(SimpleRNN(units=600, input_shape=(None, 1)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

#Load pre-trained weights
model.load_weights('model_weights.h5')

#Plot accuracy x epoch graph
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['train', 'val'], loc='upper left')
plt.show()

'''
GRU and LSTM cells
'''
#Using these elminiate vanishing gradients and make exploding gradient
#problems easier to solve

#GRU CELLS BETTER THAN SIMPLERNN

#Import modules
from keras.layers import GRU, Dense

#Print old and new model summaries
SimpleRNN_model.summary()
gru_model.summary()

#Evaluate models' performance ignore the loss value
_, acc_simpleRNN = SimpleRNN_model.evaluate(X_test, y_test, verbose=0)
_, acc_GRU = gru_model.evaluate(X_test, y_test, verbose=0)

#Print results
print("SimpleRNN model's accuracy: \t{0}".format(acc_simpleRNN))
print("GRU model's accuracy:\t{0}".format(acc_GRU))

#STACKING RNN LAYERS

#Import LSTM layer
from keras.layers.recurrent import LSTM

#Build model
model = Sequential()
model.add(LSTM(units=128, input_shape=(None, 1), return_sequences=2))
model.add(LSTM(units=128, return_sequences=2))
model.add(LSTM(units=128, return_sequences=0))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Load pre-trained weights
model.load_weights('lstm_stack_model_weights.h5')

#Print accuracy and loss
print("Loss: %0.04f\nAccuracy: %0.04f" % tuple(model.evaluate(X_test, y_test, verbose=0)))

'''
The Embedding Layer
'''

#NUMBER OF PARAMETERS COMPARISON

vocabulary_size = 80000
sentence_len = 200

#Import embedding layer
from keras.layers import Embedding

#Create model with embeddings
model = Sequential(name='emb_model')
model.add(Embedding(input_dim=vocabulary_size+1, output_dim=wordvec_dim, 
                    input_length=sentence_len, trainable=True))
model.add(GRU(128))
model.add(Dense(1))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Print summaries of one-hot model
model_onehot.summary()

#Print summaries of model with embeddings
model.summary()

#TRANSFER LEARNING

#Load glove pre-trained vectors
glove_matrix = load_glove('glove_200d.zip')

#Create a model with embeddings
model = Sequential(name='emb_model')
model.add(Embedding(input_dim=vocabulary_size+1, output_dim=wordvec_dim, 
                    embeddings_initializer=Constant(glove_matrix), 
                    input_length=sentence_len, trainable=False)) 
model.add(GRU(128))
model.add(Dense(1))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Print summaries of model
model.summary()

#EMBEDDINGS IMPROVES PERFORMANCE

#Create model with embedding
model = Sequential(name='emb_model')
model.add(Embedding(input_dim=max_vocabulary, output_dim=wordvec_dim, input_length=max_len))
model.add(SimpleRNN(units-128))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Load pre-trained weights
model.load_weights('embedding_model_weights.h5')

#Evaluate models' performance (ignore loss value)
_, acc_embeddings = model.evaluate(X_test, y_test, verbose=0)

#Print results
print("SimpleRNN model's accuracy:\t{0}\nEmbeddings model's accuracy:\t{1}".format(acc_simpleRNN, acc_embeddings))

'''
Sentiment Classification
'''

#BETTER SENTIMENT CLASSIFICATION

#Build and compile model
model = Sequential()
model.add(Embedding(vocabulary_size, wordvec_dim, trainable=True, input_length=max_text_len))
model.add(LSTM(64, return_sequences=True, dropout=0.2, recurrent_dropout=0.15))
model.add(LSTM(64, return_sequences=False, dropout=0.2, recurrent_dropout=0.15))
model.add(Dense(16))
model.add(Dropout(rate=0.25))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Load pre-trained weights
model.load_weights('model_weights.h5')

#Print loss and accuracy 
print("Loss: {0}\nAccuracy: {1}".format(*model.evaluate(X_test, y_test, verbose=0)))

#USING CNN LAYER

#Print model summary
model_cnn.summary()

#Load pre-trained weights
model_cnn.load_weights('model_weights.h5')

#Evaluate model to get loss and accuracy values
loss, acc = model_cnn.evaluate(x_test, y_test, verbose=0)

#Print loss and accuracy
print("Loss: {0}\nAccuracy: {1}".format(loss,acc))

