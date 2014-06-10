#!/usr/bin/python

import sys
import time
import datetime
from ngrams import *

def main(argv):
    in_file = argv[0]
    word_file = argv[1]
    word_dictionary = create_word_dictionary(word_file)
    onegram_book = countNgrams(in_file, 1)
    sentences = find_sentences(in_file) 
    exp_sentences = find_expliciteness(sentences, word_dictionary) 
    time1 = time.time()
    timestamp = datetime.datetime.fromtimestamp(int(time1)).strftime('%H:%M:%S')
    global output_file
    output_file = 'output_' + timestamp +'.txt'  
    write_output(exp_sentences, word_dictionary) 
    onegram_expl = countNgrams(output_file, 1)
    
    find_new_words(onegram_book, onegram_expl)


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

    
def find_new_words(book, explicit):
    for word in explicit:
        if word in book:
            ratio =  float(explicit[word]) / book[word]
            print word + '   ' + str(ratio)
        else:
            continue
    
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



def create_word_dictionary(word_file):
    dictionary = {}
    read_file = open(word_file, 'r')
    for line in read_file:
        line2 = line.strip('\n')
        line2 = line2.split(" ")
        dictionary.update({line2[0]:0})    
    read_file.close()
    return dictionary

def print_sentences(sentences):
    for i in range(0, len(sentences)):
        print('----------------')  
        print(sentences[i])
    print(len(sentences))   


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
