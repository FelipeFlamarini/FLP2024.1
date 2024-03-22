# Ler duas frases, uma em cada linha. 
# Escrever em uma linha as palavras da primeira frase que não ocorrem na segunda frase.
# Escrever em outra linha as palavras da primeira frase que oorrem na segunda frase.

frase1 = set(str(input()).lower().replace('.', '').replace(',', '').split(' '))
frase2 = set(str(input()).lower().replace('.', '').replace(',', '').split(' '))

print(frase1)
print(frase2)