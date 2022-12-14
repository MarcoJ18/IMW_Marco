import sys

def count_words(sentence):
    summary = {}
    lista = sentence.split()
    noRepeat = set(lista)
    for i in noRepeat:
        summary[i] = lista.count(i)
 

    
    return summary
        



sentence = sys.argv[1]
print(count_words(sentence))

