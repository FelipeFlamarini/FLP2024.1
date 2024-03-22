# Ler duas frases, uma em cada linha. 
# Escrever em uma linha as palavras da primeira frase que não ocorrem na segunda frase.
# Escrever em outra linha as palavras da primeira frase que ocorrem na segunda frase.

frase1 = set(str(input()).lower().replace('.', '').replace(',', '').split(' '))
frase2 = set(str(input()).lower().replace('.', '').replace(',', '').split(' '))

linha1 = [palavra for palavra in frase1 if palavra not in frase2]
linha2 = [palavra for palavra in frase1 if palavra in frase2]

print(linha1)
print(linha2)