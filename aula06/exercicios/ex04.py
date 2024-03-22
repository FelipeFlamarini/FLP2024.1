# Ler dois arquivos de texto diferentes. 
# Escrever as palavras presentes em ambos os arquivos, sem duplicatas.

with open("ex04_texto1.txt", "+r") as texto:
    palavras1 = set(str(texto.read()).lower().translate(str.maketrans('', '', ',.')).replace('\n', ' ').split(' '))

with open("ex04_texto2.txt", "+r") as texto:
    palavras2 = set(str(texto.read()).lower().translate(str.maketrans('', '', ',.')).replace('\n', ' ').split(' '))

try: 
    palavras1.remove('')
    palavras2.remove('')
except:
    pass

print(palavras1 & palavras2)