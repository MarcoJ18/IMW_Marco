import sys


n = sys.argv[1:]
max = len(n)
resultado = 0


for i in n:
    resultado += float(i)


media  = resultado / max
print(media)

