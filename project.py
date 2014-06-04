#!/usr/bin/python

import sys

def main(argv):
    in_file = argv[0]
    word_file = argv[1]
    word_dictionary = create_word_dictionary(word_file)
    print(word_dictionary)
    paragraphs = find_paragraphs(in_file)    
    # print_paragraphs(paragraphs)
    find_expliciteness(paragraphs, word_dictionary)
    
def find_paragraphs(in_file):
    read_file = open(in_file, 'r')
    paragraphs = []
    sentence = ''
    for line in read_file:
        if line != '\n':
            sentence = sentence + line
        else:
            paragraphs.append(sentence)
            sentence = ''
    paragraphs.append(sentence)
    read_file.close()     
    return paragraphs                    



def create_word_dictionary(word_file):
    dictionary = {}
    read_file = open(word_file, 'r')
    for line in read_file:
        line2 = line.strip('\n')
        dictionary.update({line2:0})    
    read_file.close()
    return dictionary

def print_paragraphs(paragraphs):
    for i in range(0, len(paragraphs)):
        print('----------------')  
        print(paragraphs[i])
    print(len(paragraphs))   


def find_expliciteness(paragraphs, word_dictionary):
    for i in range(0, len(paragraphs)):
        words = paragraphs[i].split(" ")
        for word in words:
            if word in word_dictionary:
                print(paragraphs[i])
                break
            
            
            
if __name__ == "__main__":
    main(sys.argv[1:])
