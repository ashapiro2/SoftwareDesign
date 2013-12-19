"""reducible by Aaron Shapiro"""


def make_word_dict():
    """Reads the words in words.txt and returns a dictionary
    that contains the words as keys."""
    

    d = dict()
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    for letter in ['', '', '']:
        d[letter] = letter
    return d


memo = {}
memo[''] = ['']


def reducible(word, word_dict):

    """Also adds an entry to the memo dictionary.

    A string is reducible if it has at least one child that is 
    reducible. 

    word: string
    word_dict: dictionary with words as keys
    """
    
    if word in memo:
        return memo[word]
    res = []
    for child in children(word, word_dict):
        t = is_reducible(child, word_dict)
        if t:
            res.append(child)
    memo[word] = res
    return res


def children(word, word_dict):
    """Returns a list of all words that can be formed.

    word: string

    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.

    word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.

    If there are multiple choices, returns the first one.

    word: string
    """
    if len(word) == 0:
        return
    print word,
    t = is_reducible(word, word_dict)
    
    print_trail(t[0])


def print_longest_words(word_dict):
    words = all_reducible(word_dict)
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 15 words
    for length, word in t[0:15]:
        print_trail(word)
        print '\n'


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)