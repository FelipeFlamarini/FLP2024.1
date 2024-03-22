# Ler dois arquivos de texto diferentes. 
# Escrever as palavras presentes em pelo menos um dos arquivos, sem duplicatas.

with open("ex04_texto1.txt", "+r") as texto:
    palavras = set(str(texto.read()).lower().translate(str.maketrans('', '', ',.')).replace('\n', ' ').split(' '))

with open("ex04_texto2.txt", "+r") as texto:
    palavras.update(set(str(texto.read()).lower().translate(str.maketrans('', '', ',.')).replace('\n', ' ').split(' ')))

try: 
    palavras.remove('')
except:
    pass

print(palavras)