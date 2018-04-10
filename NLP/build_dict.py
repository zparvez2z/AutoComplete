
from collections import Counter
from collections import defaultdict
import time
import sys
import pickle





with codecs.open('text_data.txt','r',encoding='utf8') as f:
    text = f.read()


corpus = text

def build_conditional_probabilities():
   

    start = time.time()
    tokenized_string = corpus
    previous_word = ' '
    dictionnary = defaultdict(list)

    for current_word in tokenized_string:
        if previous_word != '':
            dictionnary[previous_word].append(current_word)
        previous_word = current_word
        

    print("time for tokenizing:")
    end = time.time()
    print(end - start)
    
    


    for key in list(dictionnary.keys()):
        next_words = dictionnary[key]
        unique_words = set(next_words)  
        nb_words = len(next_words)
        probabilities_given_key = {}
        
        for unique_word in unique_words:
            probabilities_given_key[unique_word] = float(next_words.count(unique_word)) / nb_words
            
        dictionnary[key] = probabilities_given_key
        

    return dictionnary

start = time.time()

conditional_probabilities = buildconditional_probabilities()
dictionary = open('dictionary.obj', 'w')
pickle.dump(conditional_probabilities, dictionary)
end = time.time()
print(type(conditional_probabilities))
print(str(sys.getsizeof(conditional_probabilities)))
print(end  start)
