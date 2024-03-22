# Lista permitida. Ler um número n, seguido por n palavras "permitidas". 
# Depois, ler um número m, seguido por m frases, uma em cada linha. 
# Para cada frase, escrever "PERMITIDO" ou "CENSURADO" caso contenha apenas palavras permitidas ou não.

permitidas = set()

for n in range(int(input())):
    permitidas.add(str(input()).lower())

for m in range(int(input())):
    print("PERMITIDO") if set(str(input()).lower().translate(str.maketrans('', '', ',.')).replace('\n', ' ').split(' ')) < permitidas else print("CENSURADO")