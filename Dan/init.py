
"""
EDA with the Virginia vs. Purdue game from 2019 March Madness
@author Dan Murphy
@date Monday, February 17th, 2019
"""
import pandas
import numpy
from matplotlib import pyplot as plt
import string

# open the file
f = open("/Users/danielmurphy/Desktop/Stratifyd_IS/datasets/VirginiaVSPurdue2019CC.txt", "r")
readFile = f.read()
# verify proper reading of file
# print(readFile)

"""
Part One: word and sentence tokenization. 
First, I will remove punctuation from the textual data. 
Then, I will tokenize the cleaned data into words and sentences
"""
tab = str.maketrans('', '', string.punctuation)  # removes nothing except for punctuation
removePunctuation = readFile.translate(tab)

#tokenize sentences
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk


words = word_tokenize(removePunctuation) # word tokenization
words_with_punctuation = word_tokenize(readFile)
phrases = sent_tokenize(removePunctuation) # sentence tokenization
lower_words = [t.lower() for t in words]
lower_sentences = (t.lower() for t in phrases)

"""
Part Two: Modify our cleaned data to now remove stop words
"""
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
words_without_punctuation = word_tokenize(removePunctuation)
filtered_words = []

for word in words_without_punctuation:
    if word not in stop_words: #remove stop words
        if word not in filtered_words: #remove repeats. filtered_words is the same as words_Without_punctuation except it does not contain repeats
            filtered_words.append(word)
# print(len(words_without_punctuation))
# print(len(filtered_words))
# print(len(words_without_punctuation) - len(filtered_words))
# filtered words are now stored in filtered_words array

"""
Part Three: Stemming words using nltk.stem -> PorterStemmer
"""
from nltk.stem import PorterStemmer

porter_stemmer = PorterStemmer()

for word in filtered_words:
    (word + ": " + porter_stemmer.stem(word))


count_applause =0
count_music = 0 
applause_arr = []
music_arr = []
for word in words:
    if word == "Applause":
        count_applause += 1
        applause_arr.append(word)
    elif word == "Music":
        count_music += 1
        music_arr.append(word)
# print(count_applause + count_music)

"""
USE REGEX TO EXTRACT ANY OCCURENCE OF [a-zA-z0-9] in our data. This will show me if there
are any non-textual occurences of data outside of just music and applause!!!
"""
import re
remove_punctuation_custom = string.punctuation.replace('[', '').replace(']','')
words_filtered = readFile.translate(remove_punctuation_custom)
word_token2 = word_tokenize(words_filtered)


i = 0
unique_vals = []
all_vals = []
for word in word_token2:
    i = i + 1
    if word == "[":
        all_vals.append(word_token2[i].lower())
        if (word_token2[i] not in unique_vals):
            unique_vals.append(word_token2[i])

print(unique_vals) 
print(len(all_vals))

"""
Part Four: Graphing histogram of number of applauses and number of music segments
"""
import streamlit 
import matplotlib.pyplot as plt
import seaborn as s


# plt.hist(all_vals, color='royalblue', alpha=0.8)
# plt.title("Occurences of Non-textual Data")
# plt.xlabel("Type of Non-textual Data")
# plt.ylabel("Count")
# plt.show()


"""
Part Five: Ginding the sentences before and after the applause, laughter, and music occurrences
"""
from nltk.text import Text

textual_data = Text(lower_words)

arr = []
def concord(list, array):
    for val in list:
         print(textual_data.concordance(val, lines = 150))
        

# concord(unique_vals, arr)
# define a function to call the concordance method on the Textual version of lower_words

unique_vals = [val.lower() for val in unique_vals]
def disp_plot(data, arr):
    data.dispersion_plot(arr)

disp_plot(textual_data, unique_vals)



# count number of consonants and vowels in the data
consonant_list = ['B', 'b','C', 'c','D', 'd','F', 'f', 'G', 'g','H', 'h','J', 'j','K', 'k','L', 'l','M', 'm','N', 'n','P', 'p','Q', 'q','R', 'r','S', 's','T', 't','V', 'v','X', 'x', 'Z', 'z', 'W', 'w', 'Y', 'y']
vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

countConsonant = 0
countVowel = 0
for word in removePunctuation:
    for char in word:
        for v in vowel_list:
            if char == v:
                countVowel += 1
            else:
                for c in consonant_list:
                    if char == c:
                        countConsonant += 1
print(countConsonant)
print(countVowel)                        
