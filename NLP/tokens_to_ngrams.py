from collections import defaultdict
import codecs
import time
import pickle
start = time.time()

MIN_N_GRAM_SIZE = 5


with codecs.open('your_data.txt', 'r', encoding='utf8') as f:
    text = f.read()
exercise_names = text
token_to_exercise_name = defaultdict(list)
n_gram_to_tokens = defaultdict(set)
for exercise_name in exercise_names:
    
    tokens = exercise_name.split()
    for token in tokens:
        token_to_exercise_name[tokens].append(exercise_name)
        for string_size in range(MIN_N_GRAM_SIZE, len(token) + 1):
            n_gram = token[:string_size]
            n_gram_to_tokens[n_gram].append(token)



print(type(n_gram_to_tokens))
print(type(token_to_exercise_name))

file_handler = open('n_gram_to_tokens.obj', 'w')
pickle.dump(n_gram_to_tokens, file_handler)

file_handler = open('token_to_exercise_name.obj', 'w')
pickle.dump(token_to_exercise_name, file_handler)



print("total time : "+str(time.time()-start))
