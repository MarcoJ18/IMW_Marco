import sys

def count_words(sentence):
    summary = {}
    str_list = sentence.split()
    unique_words = set(str_list)
    print(str_list)
    print(unique_words)
    for words in unique_words:
        print(words,str_list.count(words))
        



sentence = sys.argv[1]
print(count_words(sentence))

