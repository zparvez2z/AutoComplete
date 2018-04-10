from django.shortcuts import render
from django.http import JsonResponse
from . import predict
import time
from . import corrector,AutoComplete
conditional_probabilities = predict.build_conditional_probabilities()

def index(request):
    context = {

    }
    return render(request,'index.html',context)

def autoComplete(request):
    query = request.GET.get('query',None)
    query = query.split()
    
    correct = query[-1]
    if len(correct) > 2:
        completed_words = AutoComplete.AutoCompleter().guess_exercises([correct])
        print(completed_words)

        tokens = predict.bigram_next_word_predictor(conditional_probabilities, correct)

        next_words = sorted(tokens, key=tokens.get, reverse=True)
        
        joined = [(correct + ' ' + next_word) for next_word in next_words]
        total = completed_words + joined

        
        return JsonResponse(total, safe=False)
    else:
        return JsonResponse([correct], safe=False)


