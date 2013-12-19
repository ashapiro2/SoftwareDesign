"""

Rotate Pairs by Aaron Shapiro

"""

from rotate import rotate_word


def word_dict():
    """Takes words from .txt file and returns them as a dictionary"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def rotate_word(word, word_dict):
    """Prints all words that can be generated by roating words from dictionary.

    word: string
    word_dict: dictionary with words as keys
    """
    for i in range(i, 20):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print word, i, rotated


if __name__ == '__main__':
    word_dict = make_word_dict()

    for word in word_dict:
        rotate_pairs(word, word_dict)
