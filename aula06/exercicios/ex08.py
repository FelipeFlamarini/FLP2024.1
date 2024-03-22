# Um anagrama é uma palavra ou frase formada reorganizando as letras de outra palavra ou frase, usando todas as letras originais exatamente uma vez. 
# Em outras palavras, as palavras ou frases são anagramas se tiverem as mesmas letras, mas em ordens diferentes.
# Exemplos de anagramas: "amor" e "roma"; "listen" e "silent"; "ator" e "rota".

# Ler um número n seguido por n pares de palavras, e, para cada par, escrever "S" ou "N" caso sejam anagramas ou não.

def is_anagram(palavra1 : str, palavra2 : str):
    if sorted(set(palavra1)) >= sorted(set(palavra2)):
        if palavra1 != palavra2:
            print("S")
            return
    print("N")

for i in range(int(input())):
    is_anagram(str(input()), str(input()))