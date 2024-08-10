from collections import defaultdict


## funções
def replace_nth(string: str, sub: str, n: int) -> str:
    string.find


## resolvendo exercício
## recebendo palavras ignoradas
palavras_ignoradas = set()

while True:
    palavra_input = str(input())
    if palavra_input == "::":
        break
    palavras_ignoradas.add(palavra_input.lower())

## recebendo títulos
## para finalizar envio dos títulos, enviar string vazia
titulos_input = list()

while True:
    titulo_input = str(input())
    if titulo_input == "":
        break
    titulos_input.append(titulo_input.lower())

## criando json com as palavras-chave
## key: palavra-chave
## valor: set[titulos]
palavras_chave = defaultdict(list)

for titulo in titulos_input:
    for palavra_titulo in titulo.split():
        if palavra_titulo not in palavras_ignoradas:
            palavras_chave[palavra_titulo].append(titulo)

for palavra_chave in sorted(palavras_chave.keys()):
    ## removendo frases com palavras-chave repetidas
    ## para verificar se há palavra-chave repetida na frase, basta olhar na própria frase, ao invés de ter ela várias vezes na lista
    for titulo in list(dict.fromkeys(palavras_chave[palavra_chave])):
        palavra_chave_count = titulo.count(palavra_chave)
        if palavra_chave_count < 1:
            print(titulo.replace(palavra_chave, palavra_chave.upper()))
            break
        ## quando há mais de uma palavra-chave igual no mesmo título5
        titulo_last = 0
        for i in range(palavra_chave_count):
            titulo_last += titulo.find(palavra_chave, titulo_last)
            print(
                titulo[:titulo_last]
                + (titulo[titulo_last:]).replace(
                    palavra_chave, palavra_chave.upper(), 1
                )
            )