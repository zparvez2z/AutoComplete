import re
import codecs
import pickle

def build_conditional_probabilities():
    """
    The function takes as its input a corpus string (words separated by
    spaces) and returns a 2D dictionnary of probabilities P(next|current) of
    seeing a word "next" conditionnaly to seeing a word "current".
    """

    filehandler = open('AutoComplete/dictionary.obj', 'r')
    dictionary = pickle.load(filehandler)

    return dictionary


def bigram_next_word_predictor(conditional_probabilities, current ):
    """
    The function takes as its input a 2D dictionnary of probabilities
    P(next|current) of seeing a word "next" conditionnaly to seeing a word
    "current", the current word being read, and a next candidate word, and
    returns P(next_candidate|current).
    """

    # We look for the probability corresponding to the
    # current -> next_candidate pair

    if current in conditional_probabilities:
       # if next_candidate in conditional_probabilities[current]:
            return conditional_probabilities[curent]

    # If current -> next_candidate pair has not been observed in the corpus,
    # the corresponding dictionnary keys will not be defined. We return
    # a probability 0.0

    return {'':1}


