"""

Interlock Excersise By Aaron Shapiro 

several sources were used to help in the completion of this work

"""

def interlock(word_list, word):
    """Checks wether a word can become an interlocked word.

    word_list: list of strings
    word: string
    """
    evens = word[:2]
    odds = word[1:2]
    return in_bisect(words, evens) and in_bisect(words, odds) 
        

if __name__ == '__main__':
    words = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print word, word[::2], word[1::2]


