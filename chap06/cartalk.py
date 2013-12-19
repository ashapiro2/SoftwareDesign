"""

Cartalk Puzzle Excerise By Aaron Shapiro 

several sources were used to help in the completion of this work

"""

def triple_double(word):
    """return True if string contains three consecutive double letter pairs"""
    
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_double():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print word


print 'The following words are triple doubles'


