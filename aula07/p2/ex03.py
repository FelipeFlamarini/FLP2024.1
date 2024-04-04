# (50% pontos) Desenvolva um programa que realize as seguintes tarefas:
# 1. Lê o caminho para um arquivo de texto.
# 2. Abre o arquivo especificado e escreve seu conteúdo na tela, enumerando cada linha.
# 3. Lê o número da linha a ser removida do arquivo.
# 4. Remove a linha selecionada do arquivo.
# 5. Salva o arquivo atualizado, agora sem a linha removida.

def remover_linha(caminho_arquivo : str, numero_da_linha : int):
    with open(caminho_arquivo, 'r+') as arquivo_texto:
        texto = arquivo_texto.readlines()
        texto.remove(texto[numero_da_linha - 1])

        arquivo_texto.seek(0)
        arquivo_texto.truncate()
        arquivo_texto.writelines(str().join(texto))

remover_linha(str(input('Digite o caminho do arquivo a ser modificado: ')), int(input('Digite o número da linha a ser removido: ')))