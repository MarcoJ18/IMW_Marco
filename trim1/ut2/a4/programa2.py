import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

adenine = 0
guanine = 0
cytosine = 0
thyimine = 0

for i in sequence:
    if i == 'A':
        adenine += 1
    elif i == 'G':
        guanine += 1
    elif i == 'C':
        cytosine += 1
    elif i == 'T':
        thyimine += 1
    
    
print(f'''Adenine:{adenine}
Thymine:{thyimine}
Cytosine:{cytosine}
Guanine:{guanine}''')
    