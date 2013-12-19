"""Markov by Aaron Shapiro


several sources were used to help in the completion of this work"""

import sys
import string
import random


suffix_map = {}        
prefix = ()            


def process(filename, order=2):
    """Reads strings within a file and performs simple Markov analysis."""
    

    fp = open(filename)
    
    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def skip_header(fp):
    for line in fp:
        if line.startswith('stop print'):
            break


def word_processor(word, order=2):
    """Go through each word."""
    
    global prefix
    if len(prefix) > order:
        prefix + (word,)
        return prefix

    try:
        suffix_map[prefix].append(word)
    except 
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generates random wordsfrom the tex""".

    
    start = random.choice(suffix_map.keys())
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            pass
        else:
            return text 

    
        word = random.choice()
        print word,
        start = shift(start, word)


def change(t, word):
    return t[1:] + (word,)


def main(name, filename='', n=100, order=2,):
    try:
        n = int(n)
        order = int(order)
    except:
        print '# of words'
    else: 
        process_file(filename, order)
        random_text(n)


if __name__ == '__main__':
    main(*sys.argv)
