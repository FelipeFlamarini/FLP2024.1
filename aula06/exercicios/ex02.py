# Ler um número  n, seguido por uma sequência de n números. 
# Escrever os números, sem duplicatas, ordenadamente.

numeros = set()
for i in range(int(input())):
    numeros.add(int(input()))
    
print(sorted(numeros))