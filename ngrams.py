#!/usr/bin/python

import sys
import time

# The main function which handles the arguments, finds all ngrams and outputs the
# m most frequent ngrams.
def main(argv):

    # Check passed arguments.
    if (len(argv) < 4 or len(argv) > 6) or len(argv) % 2 != 0:
        printError()

    # Initialize the passed arguments.
    else:
        # Start timing.
        start = time.clock()
        corpus = ''
        n = 0
        m = 0
        i = 0
        while (i < len(argv)):
            if argv[i] == '-corpus':
                corpus = argv[i+1]
            elif argv[i] == '-n':
                try:
                    n = int(argv[i+1])
                except ValueError:
                    printError()
            elif argv[i] == '-m':
                try:
                    m = int(argv[i+1])
                except ValueError:
                    printError()
            i += 1
        if corpus == '':
            printError()
        elif n == 0:
            printError()
        else:
            # Feedback on the passed arguments to the user.
            print 'Corpus =', corpus, ', n =', n
            print 'OPTIONAL: m =', m, '\n'
    
    # Find and count all ngrams.
    nGrams = countNgrams(corpus, n)
    # Print the m most frequent ngrams.
    printMostFrequent(nGrams, m)

    # Stop timing and print the the time in took to run the program.
    stop = time.clock()
    print '\nTime it took to run the program:', stop - start, 'second(s)\n'

# This function creates a dictionary of all unique ngrams together with the
# frequency of their appearance.
def countNgrams(corpus, n):

    # Open the file with the corpus and store all the words from the corpus in a list.
    f = open(corpus, 'r')
    dictionary = []
    for line in f:
        for word in line.split():
            dictionary.append(word)
    f.close()

    # Find all the ngrams of size n and store them in a dictionary.
    # When an ngram is already in the dictionary, then increment
    # the appearance.
    nGrams = {}
    for i in range(0, len(dictionary) - (n-1)):
        name = dictionary[i];
        for j in range(1, n):
            name = name + " " + dictionary[i+j]
        if name in nGrams:
            nGrams.update({name:(nGrams[name]+1)})
        else:
            nGrams.update({name:1})
    return nGrams

# This function outputs the m most frequent ngrams in `nGrams' (the dictionary with all
# the ngrams of size n, see the function `countNgrams').
def printMostFrequent(nGrams, m):   
    print '\n'
    # Order the ngrams according to the ngram frequencies (most frequent ngram first).
    sorted_nGrams = sorted(nGrams.items(), key=lambda nGram: nGram[1], reverse=True)

    # Print the m most frequent ngrams.
    for i in range(0, m):
        if sorted_nGrams[i][0] != '':
            print sorted_nGrams[i]
        
    print '\n'

# This function handles the error if the command line isn't used correctly; the function
# prints the correct usage and exits the program.
def printError():

    print 'Usage: ./a1-step1 -corpus [path] -n [value] -m [value]'
    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
