from collections import Counter
import codecs
import pickle
import time
import sys
start = time.time()
with codecs.open('your_data.txt','r',encoding='utf8') as f:
    text = f.read()
print("read time : "+str(time.time()-start))
corpus = text
print("spliting time : "+str(time.time()-start))
WORDS = Counter(corpus)
SWords = sorted(WORDS, key=WORDS, reverse=True)
#print(SWords)
print("Counter time : "+str(time.time()-start))
print(type(SWords))
print(str(sys.getsizeof(SWords)))

file_handler = open('word_frequency.obj', 'wb')
pickle.dump(WORDS, file_handler)

print("total time : "+str(time.time()-start))


