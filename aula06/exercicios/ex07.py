# Um heterograma é uma palavra ou frase em que nenhuma letra do alfabeto ocorre mais de uma vez.
# Ler um número n, seguido por n frases, uma em cada linha. Para cada frase, escrever "S" ou "N" caso seja heterograma ou não.

def is_heterogram(frase : str):
    ocorrencia = []
    for char in frase:
        if char.isalpha():
            if char in ocorrencia:
                print("N")
                return
            ocorrencia.append(char)
    print("S")

for i in range(int(input())):
    is_heterogram(str(input()))