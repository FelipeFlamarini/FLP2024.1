# Ler uma sequência de números, que se encerra com um número repetido. 
# Escrever os números ordenadamente.

numeros = set()
while True:
    n = int(input())
    if n in numeros:
        break
    numeros.add(n)
    
print(sorted(numeros))