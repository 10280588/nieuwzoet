#!/usr/bin/python

import sys
import time
import datetime
from ngrams import *
import string


# main function that reads the arguments and
# executes all functions
def main(argv):
    in_file = argv[0]
    word_file = argv[1]
    word_dictionary = create_word_dictionary(word_file) 
    # Find frequencie of all words
    onegram_book = countNgrams(in_file, 1)
    # Split text into an array of sentences
    sentences = find_sentences(in_file) 
    exp_sentences = find_expliciteness(sentences, word_dictionary) 
    time1 = time.time()
    # Create a timestamp for the name of the output file
    timestamp = datetime.datetime.fromtimestamp(int(time1)).strftime('%H:%M:%S')
    global output_file
    output_file = 'output_' + timestamp +'.txt'  
    # Write output to a .txt
    write_output(exp_sentences, word_dictionary) 
    # Find frequencies of all words in explicit sentences
    onegram_expl = countNgrams(output_file, 1)
    # Find new words to add to the list
    find_new_words(onegram_book, onegram_expl)
   

# Writes output to text file
def write_output(exp_sentences, word_dictionary): 
    output = open(output_file,'w')
    for i in range(0, len(exp_sentences)):
        new_sentence = ''
        words = exp_sentences[i].split(" ")
        for word in words:
            if word in word_dictionary:
                new_word = word.upper()
            else:
                new_word = word
            new_sentence = new_sentence + new_word + ' '
        output.write(new_sentence)
        output.write('\n---------\n') 
    output.close()          

# Finds new words to put in the wordlist
# Calculate ratio of frequencies when found in the 
# explicit sentences and in the total text 
def find_new_words(book, explicit):
    for word in explicit:
        if word in book:
            new_word = ''
            for letter in word:
                if letter.isalpha():
                    new_word = new_word + letter
            new_word = new_word.upper()
            ratio =  float(explicit[word]) / book[new_word]
            print new_word + '\t\t' + str(ratio)
        else:
            continue
            
# Splits text on a dot and saves it as a list of sentences    
def find_sentences(in_file):
    read_file = open(in_file, 'r')
    sentences = []
    sentence = ''
    for line in read_file:
        for word in line.split(" "):
            if not '.' in word:
                sentence = sentence + word + ' '
            else:
                sentence = sentence + word
                sentences.append(sentence)
                sentence = ''
    sentences.append(sentence)
    read_file.close()     
    return sentences                    
    
# Reads word list and saves it as a dictionary
def create_word_dictionary(word_file):
    dictionary = {}
    read_file = open(word_file, 'r')
    for line in read_file:
        line2 = line.strip('\n')
        line2 = line2.split(" ")
        dictionary.update({line2[0]:0})    
    read_file.close()
    return dictionary

# Prints a list of sentences in a neat way
def print_sentences(sentences):
    for i in range(0, len(sentences)):
        print('----------------')  
        print(sentences[i])
    print(len(sentences))   

# Finds explicit sentences by checking if words in the sentences
# are present in the word list
def find_expliciteness(sentences, word_dictionary):
    exp_sentence = []
    for i in range(0, len(sentences)):
        words = sentences[i].split(" ")
        for word in words:
            if word in word_dictionary and sentences[i] not in exp_sentence:
                exp_sentence.append(sentences[i])
                break
    return exp_sentence
            
            
            
if __name__ == "__main__":
    main(sys.argv[1:])
