## recebendo palavras ignoradas
import sys

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

## encontrando palavras-chave
palavras_chave = set()

for titulo in titulos_input:
    for palavra in titulo.split():
        if palavra not in palavras_ignoradas:
            palavras_chave.add(palavra)

palavras_chave = sorted(palavras_chave)

## verificando palavras-chave nos titulos
titulos_output = list()

for palavra_chave in palavras_chave:
    for titulo in titulos_input:
        titulo_split = titulo.split()
        for index, palavra_titulo in enumerate(titulo_split):
            if palavra_titulo == palavra_chave:
                titulo_split[index] = palavra_titulo.upper()
                titulos_output.append(" ".join(titulo_split))
                ## se essa palavra-chave não aparece de novo, não precisa continuar verificação
                if palavra_chave not in titulo_split:
                    break
                ## se essa palavra-chave aparece de novo, o que virou upper volta para lower
                titulo_split[index] = palavra_titulo.lower()

for titulo_output in titulos_output:
    print(titulo_output)
