# Lista proibida. Ler um número n, seguido por n palavras "proibidas". 
# Depois, ler um número m, seguido por m frases, uma em cada linha. 
# Para cada frase, escrever "PERMITIDO" ou "CENSURADO" caso haja palavras proibidas ou não.

proibidas = set()

for n in range(int(input())):
    proibidas.add(str(input()).lower())

for m in range(int(input())):
    print("PERMITIDO") if set(str(input()).lower().translate(str.maketrans('', '', ',.')).replace('\n', ' ').split(' ')).isdisjoint(proibidas) else print("CENSURADO")