#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:58:31 2020

@author: owenbezick

Introduction to regular expressions datacamp course notes chapter 1.
"""

import re

# match a substring
re.match('abc', 'abcdef')
# Out: <re.Match object; span=(0, 3), match='abc'>

# match a word
word_regex = '\w+'
re.match(word_regex, 'hi there!')
# Out: <re.Match object; span=(0, 2), match='hi'>

""" 
common patterns:
\w words
\d digits
\s space
\. wildcard - will pick up anything
+ or * greedy
capital letters negates the patterns
can group using square brackets 

split, findall, search, match
pattern first, the string second
may return iterator, string, or match object
"""

my_string = "Let's write RegEx!"
PATTERN = r"\s+"
re.findall(PATTERN, my_string)
PATTERN = r"\w+"
re.findall(PATTERN, my_string)
PATTERN = r"[a-z]"
re.findall(PATTERN, my_string)
PATTERN = r"\w"
re.findall(PATTERN, my_string)
"""
Note: It's important to prefix your regex patterns with r to ensure that your 
      patterns are interpreted in the way you want them to. Else, you may 
      encounter problems to do with escape sequences in strings. For example,
      "\n" in Python is used to indicate a new line, but if you use the r prefix, 
      it will be interpreted as the raw string "\n" - that is, the character "\" 
      followed by the character "n" - and not as a new line.
"""
# Write a pattern to match sentence endings: sentence_endings
my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"

sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result: (.?!)
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result
spaces = r"\s"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))

"""
Tokenization: turning a string or document into tokens (smaller chunks).
Can create your own rules using regulare expressions.
Examples include: breaking out words or sentences, seperating punctuation or all hashtags in a tweet.

natural language toolkit library

sent_tokenize: tokenize a document into sentences
regexp_tokenize: tokenize a string or document based on a regular expression pattern
TweetTokenizer: special class just for tweet tokenization, allowing you to separate hashtags, mentions, etc.

# In order to use the following commands locally, pip install nltk, then in your
# python console, import nltk, run nltk.download(), then in the window that appears
# go to models, punkt, then download. Voila.

"""
from nltk.tokenize import word_tokenize
word_tokenize("Hi there!") 

# re.serach() vs re.match()
# pattern that might not be at beginning > use search
# be specific abt composition about entire string or atleast initial pattern > use match

re.match('abc', 'abcde')
#<_sre.SRE_Match object; span=(0, 3), match='abc'>

re.search('abc', 'abcde')
# <_sre.SRE_Match object; span=(0, 3), match='abc'>

re.match('cd', 'abcde')
# No output
re.search('cd', 'abcde')
# <_sre.SRE_Match object; span=(2, 4), match='cd'>

scene_one = "SCENE 1: [wind] [clop clop clop] \
\n KING ARTHUR: Whoa there!  [clop clop clop] \
\n SOLDIER #1: Halt!  Who goes there? \
\n ARTHUR: It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign of all England! \
\n SOLDIER #1: Pull the other one! \
\n ARTHUR: I am, ...  and this is my trusty servant Patsy.  We have ridden the length and breadth of the land in search of knights who will join me in my court at Camelot.  I must speak with your lord and master. \
\n SOLDIER #1: What?  Ridden on a horse? \
\n ARTHUR: Yes! \
\n SOLDIER #1: You're using coconuts! \
\n ARTHUR: What?\
\n SOLDIER #1: You've got two empty halves of coconut and you're bangin' 'em together.\
\n ARTHUR: So?  We have ridden since the snows of winter covered this land, through the kingdom of Mercea, through-- \
\n SOLDIER #1: Where'd you get the coconuts? \
\n ARTHUR: We found them. \
\n SOLDIER #1: Found them?  In Mercea?  The coconut's tropical! \
\n ARTHUR: What do you mean? \
\n SOLDIER #1: Well, this is a temperate zone. \
\n ARTHUR: The swallow may fly south with the sun or the house martin or the plover may seek warmer climes in winter, yet these are not strangers to our land? \
\n SOLDIER #1: Are you suggesting coconuts migrate? \
\n ARTHUR: Not at all.  They could be carried. \
\n SOLDIER #1: What?  A swallow carrying a coconut? \
\n ARTHUR: It could grip it by the husk! \
\n SOLDIER #1: It's not a question of where he grips it!  It's a simple question of weight ratios!  A five ounce bird could not carry a one pound coconut. \
\n ARTHUR: Well, it doesn't matter.  Will you go and tell your master that Arthur from the Court of Camelot is here. \
\n SOLDIER #1: Listen.  In order to maintain air-speed velocity, a swallow needs to beat its wings forty-three times every second, right? \
\n ARTHUR: Please! \
\n SOLDIER #1: Am I right?\
\n ARTHUR: I'm not interested!\
\n SOLDIER #2: It could be carried by an African swallow!\
\n SOLDIER #1: Oh, yeah, an African swallow maybe, but not a European swallow.  That's my point.\
\n SOLDIER #2: Oh, yeah, I agree with that.\
\n ARTHUR: Will you ask your master if he wants to join my court at Camelot?!\
\n SOLDIER #1: But then of course a-- African swallows are non-migratory.\
\n SOLDIER #2: Oh, yeah...\
\n SOLDIER #1: So they couldn't bring a coconut back anyway...  [clop clop clop] \
\n SOLDIER #2: Wait a minute!  Supposing two swallows carried it together?\
\n SOLDIER #1: No, they'd have to have it on a line.\
\n SOLDIER #2: Well, simple!  They'd just use a strand of creeper!\
\n SOLDIER #1: What, held under the dorsal guiding feathers?\
\n SOLDIER #2: Well, why not?"

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)

# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*\]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1, scene_one))

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w\s]+:"
print(re.match(pattern2, sentences[3]))

"""
Advanced Tokenization with Regex

or method using | 
define groups using ()
define explicit character ranges using []

[A-Za-z]+ matches all upper and lowercase
[0-9] numbers from 0 to 9
[A-Za-z\-\.]+ upper and lower case english alphabet - and .
(a-z) a, -, and z
(\s+|,) spaces or a comma

Unlike the syntax for the regex library, with nltk_tokenize() you pass the pattern as the second argument.
"""
match_digits_and_words = ('(\d+|\w+)')
re.findall(match_digits_and_words, 'He has 11 cats.')
#Out: ['He', 'has', '11', 'cats']
my_str = 'match lowercase spaces nums like 12, but no commas'
re.match('[a-z0-9 ]+', my_str)
#Out: <_sre.SRE_Match object; 
          #span=(0, 42), match='match lowercase spaces nums like 12'>
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
"""
# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)
print(hashtags)
# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([@|#]\w+)"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)
# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)
# Tokenize and print all words in german_text
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words
capital_words = r"[A-Z|Ü]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))
"""

"""
Charting NLP charts with matplotlib

"""
from matplotlib import pyplot as plt
plt.hist([1, 5, 5, 7, 7, 7, 9])
words = word_tokenize("This is a pretty cool tool!")
word_lengths = [len(w) for w in words]
plt.hist(word_lengths)

# Split the script into lines: lines
lines = holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s, r"\w+") for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.hist(line_num_words)

# Show the plot
plt.show()

