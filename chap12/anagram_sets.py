
"""anagram sets by Aaron Shapiro

several sources were used to help in the completion of this work"""



def anagrams(filename):
    """Finds all the anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the sets in d""".

    d: map from words to list of their anagrams
    
    for v in d.values():
        if len(v) > 1:
            print len(v), v


def print_order_set(d):
    """Prints the sets in decreasing order."""

    d: map from words to list of their anagrams
    

    #make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))
    t.sort()

    # print the sorted list
    for x in t:
        print x

if __name__ == '__main__':
    d = all_anagrams('words.txt')
    print_anagram_sets_in_order(d)

    eight_letters = filter_length(d, 8)
    print_anagram_sets_in_order(eight_letters)
    
