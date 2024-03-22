# Um pangrama é uma frase em que são usadas todas as letras do alfabeto de determinada língua. 
# Exemplo de pangrama em inglês: The quick brown fox jumps over the lazy dog. 
# Exemplo de pangrama em português, desconsiderando as letras de origem saxônica: Blitz prende ex-vesgo com cheque fajuto.

# Ler um número n, seguido por n frases, uma em cada linha. 
# Para cada frase, escrever "S" ou "N" caso seja pangrama inglês ou não (desconsidera acentos).

for i in range(int(input())):
#                 set com frase do usuário    set com o alfabeto
    print("S") if set(str(input()).lower()) > set('abcdefghijklmnopqrstuvwxyz') else print("N")