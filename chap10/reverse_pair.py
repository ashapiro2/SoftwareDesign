"""
Reverse Pair by Aaron Shapiro


several sources were used to help in the completion of this work
"""

def pair_reverser(word_list, word):
    
    rev_word = word[:-1]
    return in_bisect(word_list, rev_word)
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    
    for word in word_list:
        if reverse_pair(word_list, word):
            print word, word[:-1]


